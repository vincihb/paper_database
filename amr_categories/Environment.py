from amr_categories.Themes import Themes
from amr_categories.Water import Water
import random


class Environment(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "environment"
        self.water = Water()
        self.keywords = "environment, environmental, ecology, ecological, ecosystem, ecosystems, soil".split(", ")
        self.keywords_and = "contamination, manure, manures, excreta, excrement, leach, leaching, " \
                            "lechate, pollution, run-off, runoff, wildlife, remediation, DNA, eDNA".split(", ")
        self.keywords_and = list(dict.fromkeys(self.keywords_and))
        self.surveillance = "source of resistance, run-off, wildlife, ecology, " \
                            "ecosystem, veterinary antibiotic use".split(", ") + self.surveillance
        self.surveillance = list(dict.fromkeys(self.surveillance))
        self.mitigation = "remediation".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))
        self.theme_keywords = "wildlife, remediation, removal, eDNA, environment, ecology, ecosystem, soil".split(", ")
        self.general_keywords = "contamination, manure, excrement, excreta, excrement, leach, leachate, pollution, " \
                                "run-off, runoff, sewage, feces, transmission, reservoir".split(", ")
        # keywords = self.water.keywords_to_subcategories
        # additional_keywords = []
        # for key in keywords.keys():
        #     if keywords.get(key) not in self.keywords:
        #         additional_keywords = additional_keywords + keywords.get(key)
        self.theme_keywords_not = "karst, river, lake, stream, marine, influent, drinking, potable, water, " \
                                  "wastewater, effluent, landfill, aquifer".split(", ")


if __name__ == "__main__":
    a = Environment()
    a.set_all_papers_secondary_database()
    papers = a.all_papers
    print(len(papers))
    # # i = 0
    # # for paper in papers:
    # #     if i == 10:
    # #         break
    # #     i = i + 1
    # #     print(paper)
    papers = a.get_papers_on_prevention()
    print(len(papers))
    papers = a.get_papers_on_surveillance()
    print(len(papers))
    papers = a.get_papers_on_mitigation()
    print(len(papers))
    papers = a.get_papers_on_innovation()
    print(len(papers))