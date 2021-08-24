from amr_categories.Themes import Themes


class Plants(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "plants, plant, agriculture, pesticides, herbicides, fungicides, fertilizers, " \
                        "horticulture, botany, fruit, vegetable, harvest, crop, nursery, biocide, " \
                        "leaf, legume, roots, fresh produce, manure, manures"
        self.prevention = "prevention, pesticides, herbicides, fungicides"
        self.surveillance = "surveillance"
        self.mitigation = "mitigation"

        self.keywords = self.keywords.split(", ")
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = Plants()
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
