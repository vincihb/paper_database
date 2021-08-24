from amr_categories.Themes import Themes


class Environment(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "environmental contamination, environmental AMR, pollution, source of resistance," \
                        "transmission vector, selective pressure, reservoir, resistance development, " \
                        "antibiotic concentration, run-off, wildlife, manures, manure, ecology, " \
                        "ecosystem, remediation, soil contamination, environmental DNA, eDNA"
        self.prevention = "prevention, environmental education"
        self.surveillance = "surveillance, source of resistance, run-off, " \
                            "wildlife, ecology, ecosystem, veterinary antibiotic use"
        self.mitigation = "mitigation, remediation"

        self.keywords = self.keywords.split(", ")
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = Environment()
    papers = a.get_all_papers()
    print(len(papers))
    papers = a.get_papers_on_prevention()
    print(len(papers))
    papers = a.get_papers_on_surveillance()
    print(len(papers))
    papers = a.get_papers_on_mitigation()
    print(len(papers))
    papers = a.get_papers_on_innovation()
    print(len(papers))
