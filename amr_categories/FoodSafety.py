from amr_categories.Themes import Themes


class FoodSafety(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "food supply, food supplies, food safety, food security, food handling, food processing, " \
                        "street food, food contamination, food production, food retail, food import, " \
                        "food imports, food exports, food export, food system, food systems, grocery, groceries " \
                        "food packaging, foodborne, food borne, food surfaces, supply chain, industrial hygiene"
        self.prevention = "prevention, sanitization, pasteurization"
        self.surveillance = "surveillance"
        self.mitigation = "mitigation, sanitization, pasteurization"

        self.keywords = self.keywords.split(", ")
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = FoodSafety()
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
