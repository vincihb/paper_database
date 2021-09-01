from data.PaperCache import PaperCache


class Themes:
    def __init__(self, all_papers=None):
        self.pc = PaperCache()

        self.keywords = [""]
        self.prevention = "prevention, prescribing practice, prescribing practices, education, awareness, training"
        self.mitigation = "mitigation, removal, treatment, treatments, policy, policies, regulation, regulations, " \
                          "standard, standards, reduction, protocol, protocols, guideline, guidelines, strategy, " \
                          "strategies, stewardship"
        self.surveillance = "surveillance, transmission, presence, prevalence, monitoring, screening, susceptibility " \
                            "testing, emergence, occurrence, distribution, database, databases, epidemiology, " \
                            "detection, spread"
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")
        if all_papers is None:
            self.all_papers = self.pc.get_papers_from_list_of_keywords_or(self.keywords)
        else:
            self.all_papers = all_papers

        self.r_and_d = "discovery, laboratory, novel, therapeutic, innovation, innovative, new antibiotics, R&D, " \
                       "new diagnostics, accelerator, method development, tool development, drug development, " \
                       "vaccine development, clinical trial, funding, pilot, translational, biomedicine, de novo, " \
                       "alternative medicine, alternative antibiotics, technology, technological, sequence, " \
                       "error rates"
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



