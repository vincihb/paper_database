from amr_categories.Themes import Themes
from amr_categories.Water import Water


class CleanWater(Themes):
    def __init__(self):
        super().__init__()
        self.water = Water()
        self.keywords = "Clean water, water santitation, water supply, leach, leaching, " \
                        "lechate, wastewater, effluent, surface water, river, lake, stream, " \
                        "marine water, groundwater, influent, drinking water, portable water, " \
                        "water use, water treatment, wastewater treatment, water filtration, " \
                        "wastewater filtration, chlorination, ultraviolet, oxidation, WASH"
        self.prevention = "prevention, water treatment, wastewater treatment, water filtration, " \
                          "wastewater filtration, chlorination, ultraviolet, oxidation"
        self.surveillance = "surveillance, leach, leaching, lechate, wastewater, effluent"
        self.mitigation = "mitigation, water treatment, wastewater treatment, water filtration, " \
                          "wastewater filtration, chlorination, ultraviolet, oxidation, WASH"

        self.keywords = self.keywords.split(", ")
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")

        keywords = self.water.keywords_to_subcategories
        additional_keywords = []
        for key in keywords.keys():
            if keywords.get(key) not in self.keywords:
                additional_keywords = additional_keywords + keywords.get(key)
        self.keywords = self.keywords + additional_keywords
        self.keywords = list(dict.fromkeys(self.keywords))

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = CleanWater()
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
