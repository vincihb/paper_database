from data.PaperCache import PaperCache


class Themes:
    def __init__(self, all_papers=None):
        self.pc = PaperCache()
        self.database = False
        self.theme = ""
        self.keywords = [""]
        self.keywords_and = [""]
        self.theme_keywords = [""]
        self.prevention = "prevention, prescribing practice, prescribing practices, education, awareness, training".split(
            ", ")
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

    def get_papers_by_year(self, year):
        to_return = []
        for paper in self.all_papers:
            if paper.get("PUBLISHED_YEAR") == year:
                to_return.append(paper)
        return to_return

    def get_all_papers(self):
        return self.pc.get_papers_and(self.pc.get_papers_from_list_of_keywords_or(self.keywords),
                                      self.pc.get_papers_from_list_of_keywords_or(self.keywords_and))

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
        theme_keywords = self.theme_keywords
        theme_keywords = list(dict.fromkeys(theme_keywords))
        dict_of_theme = {key: 0 for key in theme_keywords}
        for keyword in keywords:
            k = keyword.get('KEYWORD')
            if k in theme_keywords:
                dict_of_theme.update({k: keyword.get('WEIGHT') + dict_of_theme.get(k)})
        return dict_of_theme

    def _get_papers_on_subject(self, subject):
        papers_1 = self.all_papers
        papers_2 = self.pc.get_papers_from_list_of_keywords_or(subject)
        if self.database:
            return self.pc.get_papers_and_themes(papers_2, papers_1)
        return self.pc.get_papers_and(papers_2, papers_1)
