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