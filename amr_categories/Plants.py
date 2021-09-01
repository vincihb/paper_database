from amr_categories.Themes import Themes


class Plants(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "usage of antimicrobials in plants, use of antimicrobials in plants, plants, agriculture, " \
                        "pesticide, pesticides, herbicide, herbicides, fungicide, fungicides, fertilizer, " \
                        "fertilizers, horticulture, botany, fruit, fruits, vegetable, vegetables, harvest, crop, " \
                        "crops, nursery, biocide, leaf, leaves, legume, legumes, roots, fresh produce, manure, " \
                        "manures, aquaculture plant, aquaculture plants, aquaculture seafood".split(", ")
        self.prevention = "prevention, pesticide, pesticides, herbicide, herbicides, fungicide, fungicides, " \
                          "prescribing practice, prescribing practices, education, awareness, training".split(", ") + \
                          self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = Plants()
    papers = a.all_papers
    print(len(papers))
    papers = a.get_papers_on_prevention()
    print(len(papers))
    papers = a.get_papers_on_surveillance()
    print(len(papers))
    papers = a.get_papers_on_mitigation()
    print(len(papers))
    papers = a.get_papers_on_innovation()
    print(len(papers))
