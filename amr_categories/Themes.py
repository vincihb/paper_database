from data.PaperCache import PaperCache
from nltk.stem import PorterStemmer


def remove_repeats(lst):
    return list(dict.fromkeys(lst))


class Themes:
    def __init__(self, all_papers=None):
        self.ps = PorterStemmer()
        self.pc = PaperCache()
        self.database = False
        self.theme = ""
        self.keywords = [""]
        self.keywords_and = [""]
        self.theme_keywords = [""]
        self.general_keywords = [""]
        self.theme_keywords_not = [""]
        self.prevention = "prevention, prescribing practice, prescribing practices, education, " \
                          "awareness, training".split(", ")
        self.surveillance = "surveillance, transmission, presence, prevalence, monitoring, screening, scoping, " \
                            "susceptibility, testing, emergence, occurrence, distribution, " \
                            "database, databases, epidemiology, " \
                            "detection, spread, trend, trends, pattern, patterns".split(", ")
        self.mitigation = "mitigation, treatment, treatments, policy, policies, regulation, regulations, standard, " \
                          "standards, reduction, protocol, protocols, guideline, guidelines, strategy, strategies, " \
                          "stewardship, behaviour change, behavior change".split(", ")
        self.r_and_d = "discovery, translational research, laboratory, novel, new, innovation, innovative, " \
                       "accelerator, incubator, method development, tool development, clinical trial, funding, pilot, " \
                       "alternative, technology, technological, investment, investments".split(", ")
        if all_papers is None:
            self.all_papers = []
        else:
            self.all_papers = all_papers

    def set_all_papers(self):
        self.all_papers = self.get_all_papers()

    def set_all_papers_primary_database(self):
        self.database = True
        self.all_papers = self.pc.get_papers_from_primary_theme(self.theme)

    def set_all_papers_secondary_database(self):
        self.database = True
        self.all_papers = self.pc.get_papers_from_secondary_theme(self.theme)

    def set_theme_keywords(self, keywords):
        self.keywords = [k for k in keywords if k not in self.theme_keywords_not]

    def set_general_keywords(self, keywords):
        self.general_keywords = [k for k in keywords if k not in self.theme_keywords_not]

    def get_papers_by_year(self, year):
        to_return = []
        for paper in self.all_papers:
            if paper.get("PUBLISHED_YEAR") == year:
                to_return.append(paper)
        return to_return

    def get_all_papers(self):
        return self.pc.get_papers_and(self.pc.get_papers_from_list_of_keywords_or(self.theme_keywords),
                                      self.pc.get_papers_from_list_of_keywords_or(self.general_keywords))

    def get_papers_on_prevention(self):
        return self._get_papers_on_subject(self.prevention)

    def get_papers_on_surveillance(self):
        return self._get_papers_on_subject(self.surveillance)

    def get_papers_on_mitigation(self):
        return self._get_papers_on_subject(self.mitigation)

    def get_papers_on_innovation(self):
        return self._get_papers_on_subject(self.r_and_d)

    def get_histogram_theme_from_paper(self, paper):
        keywords = self.pc.get_keywords_from_paper(paper)
        return self._get_histogram(keywords)

    def get_histogram_theme_from_paper_id(self, paper_id):
        keywords = self.pc.get_keywords_from_paper_id(paper_id)
        return self._get_histogram(keywords)

    def get_histogram_theme_from_paper_doi(self, paper_doi):
        keywords = self.pc.get_keywords_from_paper_doi(paper_doi)
        return self._get_histogram(keywords)

    def get_weighting_theme_from_paper(self, paper):
        dict_of_theme = self.get_histogram_theme_from_paper(paper)
        return self._get_weighting(dict_of_theme)

    def get_weighting_theme_from_paper_id(self, paper_id):
        dict_of_theme = self.get_histogram_theme_from_paper_id(paper_id)
        return self._get_weighting(dict_of_theme)

    def get_weighting_theme_from_paper_doi(self, paper_doi):
        dict_of_theme = self.get_histogram_theme_from_paper_doi(paper_doi)
        return self._get_weighting(dict_of_theme)

    @staticmethod
    def _get_weighting(dict_of_theme):
        to_return = 0
        for key in dict_of_theme.keys():
            to_return = to_return + dict_of_theme.get(key)
        return to_return

    def _get_histogram(self, keywords):
        theme_keywords = remove_repeats([self.ps.stem(a) for a in self.theme_keywords])
        theme_keywords_not = remove_repeats([self.ps.stem(a) for a in self.theme_keywords_not
                                             if (a not in self.general_keywords and a not in self.theme_keywords)])
        general_keywords = remove_repeats([self.ps.stem(a) for a in self.general_keywords])
        dict_of_theme = {key: 0 for key in theme_keywords}
        dict_of_theme_not = {key: 0 for key in theme_keywords_not}
        dict_of_general = {key: 0 for key in general_keywords}

        for keyword in keywords:
            k = self.ps.stem(keyword.get('KEYWORD'))
            if k in theme_keywords:
                dict_of_theme.update({k: keyword.get('WEIGHT') * 1 + dict_of_theme.get(k)})
        if sum(dict_of_theme.values()) == 0:
            dict_of_theme.update(dict_of_theme_not)
            dict_of_theme.update(dict_of_general)
            return dict_of_theme
        for keyword in keywords:
            k = self.ps.stem(keyword.get('KEYWORD'))
            if k in general_keywords:
                dict_of_general.update({k: keyword.get('WEIGHT') * 1 + dict_of_general.get(k)})
                # dict_of_general.update({k: 1})
        # if sum(dict_of_general.values()) == 0:
        #     dict_of_theme = {k: 0 for k in self.theme_keywords}
        #     dict_of_theme.update(dict_of_theme_not)
        #     dict_of_theme.update(dict_of_general)
        #     return dict_of_theme
        for keyword in keywords:
            k = self.ps.stem(keyword.get('KEYWORD'))
            if k in theme_keywords_not:
                dict_of_theme_not.update({k: keyword.get('WEIGHT') * -1 + dict_of_theme_not.get(k)})
                # dict_of_theme_not.update({k: -1})
        # print(self.theme)
        # print(dict_of_theme)
        # print(dict_of_general)
        # print(dict_of_theme_not)
        # print("=======")
        dict_of_theme.update(dict_of_theme_not)
        dict_of_theme.update(dict_of_general)
        return dict_of_theme

    def _get_papers_on_subject(self, subject):
        s = remove_repeats([self.ps.stem(a) for a in subject])
        to_return = []
        papers_1 = self.all_papers
        for paper in papers_1:
            if subject == self.surveillance:
                if self.pc.get_countries_from_paper_id(paper.get('ID')):
                    to_return.append(paper)
                    continue
            keywords = remove_repeats([self.ps.stem(k.get('KEYWORD'))
                                       for k in self.pc.get_keywords_from_paper_id(paper.get('ID'))])
            for keyword in s:
                if keyword in keywords:
                    to_return.append(paper)
                    break
        return to_return
