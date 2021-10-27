from amr_categories.Themes import Themes


class FoodSafety(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "food"
        self.keywords = "supply, safety, security, contamination, production, supply chain, handling, processing, " \
                        "slaughter, butcher, butchery, surfaces, hygiene, packaging, import, export, retail, street, " \
                        "grocery, ".split(", ")
        self.keywords_and = "food, foodborne, food-borne".split(", ")
        self.prevention = "pasteurization, pasteurisation, pasteurize, pasteurise".split(", ") + self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))
        self.mitigation = "sanitization, pasteurization".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))
        self.theme_keywords = "slaughter, butcher, butchery, packaging, retail, street, grocery, food, foodborne, " \
                              "food-borne, pork, beef, dairy, mutton, meat, seafood, shops, store, market, " \
                              "food-producing, slaughterhouse".split(", ")
        self.general_keywords = "contamination, surface, hygiene, animal, chickens, farm, consumption, supply, " \
                                "safety, security, production, chain, handling, processing, import, export".split(", ")
        # self.theme_keywords_not = "infection, prevention, control, personal, protective, equipment, PPE, " \
        #                           "disinfection, sterilization, sanitization, washing, mask".split(", ")


if __name__ == "__main__":
    a = FoodSafety()
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
