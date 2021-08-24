from data.PaperCache import PaperCache


class Themes:
    def __init__(self, all_papers=None):
        self.pc = PaperCache()

        self.keywords = [""]
        self.prevention = ""
        self.mitigation = ""
        self.surveillance = ""
        if all_papers is None:
            self.all_papers = self.pc.get_papers_from_list_of_keywords_or(self.keywords)
        else:
            self.all_papers = all_papers

        self.r_and_d = "discovery, laboratory, novel, therapeutic, research, innovation, innovative, " \
                       "new antimicrobials, R&D, new diagnostics, new classes of medication, accelerator, " \
                       "method development, tool development, drug development, vaccine development, clinical trial, " \
                       "push funding, pull funding, in vitro, pipeline, pilot, translational, biomedicine, de novo, " \
                       "database, alternative medicine, complementary medicine"
        self.r_and_d = self.r_and_d.split(", ")

    def get_papers_by_year(self, year):
        to_return = []
        for paper in self.all_papers:
            if paper.get("PUBLISHED_YEAR") == year:
                to_return.append(paper)
        return to_return

    def get_all_papers(self):
        return self.pc.get_papers_from_list_of_keywords_or(self.keywords)

    def get_papers_on_prevention(self):
        return self._get_papers_on_subject(self.prevention)

    def get_papers_on_surveillance(self):
        return self._get_papers_on_subject(self.surveillance)

    def get_papers_on_mitigation(self):
        return self._get_papers_on_subject(self.mitigation)

    def get_papers_on_innovation(self):
        return self._get_papers_on_subject(self.r_and_d)

    def _get_papers_on_subject(self, subject):
        papers_1 = self.all_papers
        papers_2 = self.pc.get_papers_from_list_of_keywords_or(subject)
        return self.pc.get_papers_and(papers_1, papers_2)



