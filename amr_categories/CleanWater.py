from amr_categories.Themes import Themes
import random


class CleanWater(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "water"
        # self.water = Water()
        self.keywords = "contamination, manure, manures, excreta, excrement, leach, leaching, lechate, pollution, " \
                        "transmission vector, selective pressure, run-off, runoff, clean, santitation, supply, " \
                        "environmental, source, surface, river, lake, stream, marine, groundwater, influent, " \
                        "drinking, potable, treatment, removal, filtration, chlorination, ultraviolet, oxidation, " \
                        "WASH".split(", ")
        self.keywords_and = "water, waters, wastewater, wastewaters, sewage, effluent, landfill".split(", ")
        self.mitigation = "filtration, chlorination, ultraviolet, oxidation".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))

        # keywords = self.water.keywords_to_subcategories
        # additional_keywords = []
        # for key in keywords.keys():
        #     if keywords.get(key) not in self.keywords:
        #         additional_keywords = additional_keywords + keywords.get(key)
        # self.keywords = self.keywords + additional_keywords
        # self.keywords = list(dict.fromkeys(self.keywords))
        self.theme_keywords = "karst, river, lake, stream, marine, ground, influent, drinking, potable, water, " \
                              "wastewater, waste, sewage, effluent, landfill, aquifer".split(", ")
        self.general_keywords = "contamination, manure, excrement, excreta, excrement, leach, leachate, pollution, " \
                                "run-off, runoff, feces, treatment, removal, filtration, chlorination, ultraviolet, " \
                                "irradiation, oxidation, transmission, clean, sanitation, supply, environment, " \
                                "source, surface, reservoir".split(", ")
        self.theme_keywords_not = "wildlife, eDNA, environment, ecology, ecosystem, soil".split(", ")


if __name__ == "__main__":
    a = CleanWater()
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
