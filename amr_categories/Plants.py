from amr_categories.Themes import Themes


class Plants(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "plants"
        self.keywords = "antibiotic, antimicrobial, antibacterial, antibiotics, antimicrobials, antibacterials, " \
                        "anti-biotic, anti-microbial, anti-bacterial, multidrug resistance, multi-drug resistance, " \
                        "pan-drug, pandrug, use, usage, pesticide, pesticides, herbicide, herbicides, fungicide, " \
                        "fungicides, biocide, fertilizer, fertilizers, manure, manures, farm, agriculture, " \
                        "agricultural, aquaculture, aquacultural, pond, tank, nursery, horticulture, harvest".split(", ")
        self.keywords_and = "plant, plants, fruit, fruits, vegetable, vegetables, crop, crops, leaf, leaves, legume, " \
                            "legumes, root, roots, fresh produce, seaweed, kelp, algae".split(", ")
        self.prevention = "pesticide, pesticides, herbicide, herbicides, fungicide, fungicides".split(", ") + \
                          self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))


if __name__ == "__main__":
    a = Plants()
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
