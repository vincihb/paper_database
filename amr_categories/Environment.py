from amr_categories.Themes import Themes


class Environment(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "environment"
        self.keywords = "environment, environmental, ecology, ecological, ecosystem, ecosystems, soil".split(", ")
        self.keywords_and = "contamination, manure, manures, excreta, excrement, leach, leaching, " \
                            "lechate, pollution, run-off, runoff, wildlife, remediation, DNA, eDNA".split(", ")
        self.keywords_and = list(dict.fromkeys(self.keywords_and))
        self.surveillance = "source of resistance, run-off, wildlife, ecology, " \
                            "ecosystem, veterinary antibiotic use".split(", ") + self.surveillance
        self.surveillance = list(dict.fromkeys(self.surveillance))
        self.mitigation = "remediation".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))


if __name__ == "__main__":
    a = Environment()
    a.set_all_papers_primary_database()
    papers = a.all_papers
    print(len(papers))
    # i = 0
    # for paper in papers:
    #     if i == 10:
    #         break
    #     i = i + 1
    #     print(paper)
    papers = a.get_papers_on_prevention()
    print(len(papers))
    papers = a.get_papers_on_surveillance()
    print(len(papers))
    papers = a.get_papers_on_mitigation()
    print(len(papers))
    papers = a.get_papers_on_innovation()
    print(len(papers))