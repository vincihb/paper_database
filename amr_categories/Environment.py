from amr_categories.Themes import Themes


class Environment(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "environmental contamination, environmental AMR, pollution, source of resistance, " \
                        "transmission vector, selective pressure, reservoir, resistance development, antibiotic " \
                        "concentration, manure, manures, run-off, wildlife, ecology, ecosystem, remediation, " \
                        "soil contamination, environmental DNA, eDNA".split(", ")
        self.surveillance = "surveillance, source of resistance, run-off, wildlife, ecology, ecosystem, veterinary " \
                            "antibiotic use, transmission, presence, prevalence, monitoring, screening, " \
                            "susceptibility testing, emergence, occurrence, distribution, database, databases, " \
                            "epidemiology, detection, spread".split(", ") + \
                            self.surveillance
        self.mitigation = "mitigation, remediation, removal, treatment, treatments, policy, policies, regulation, " \
                          "regulations, standard, standards, reduction, protocol, protocols, guideline, guidelines, " \
                          "strategy, strategies, stewardship".split(", ") + self.mitigation

        self.surveillance = list(dict.fromkeys(self.surveillance))
        self.mitigation = list(dict.fromkeys(self.mitigation))

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
