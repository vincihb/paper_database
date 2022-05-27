from amr_categories.Themes import Themes
from amr_categories.Water import Water


class Plants(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "plants"
        self.water = Water()
        self.keywords = "antibiotic, antimicrobial, antibacterial, antibiotics, antimicrobials, antibacterials, " \
                        "anti-biotic, anti-microbial, anti-bacterial, multidrug resistance, multi-drug resistance, " \
                        "pan-drug, pandrug, use, usage, pesticide, pesticides, herbicide, herbicides, fungicide, " \
                        "fungicides, biocide, fertilizer, fertilizers, manure, manures, farm, agriculture, " \
                        "agricultural, aquaculture, aquacultural, pond, tank, " \
                        "nursery, horticulture, harvest".split(", ")
        self.keywords_and = "plant, plants, fruit, fruits, vegetable, vegetables, crop, crops, leaf, leaves, legume, " \
                            "legumes, root, roots, fresh produce, seaweed, kelp, algae".split(", ")
        self.prevention = "pesticide, pesticides, herbicide, herbicides, fungicide, fungicides".split(", ") + \
                          self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))
        self.theme_keywords = "use, usage, consumption, consume, prescribe, overuse, misuse, treatment, dosage, " \
                              "access, practice, prescription, stewardship, immunization, vaccine, behaviour, " \
                              "behavior".split(", ")
        self.general_keywords = "pesticide, herbicide, fungicide, biocide, fertilizer, manure, farm, agriculture, " \
                                "agricultural, aquaculture, aquacultural, pond, tank, nursery, horticulture, harvest, " \
                                "plant, fruit, vegetable, crop, leaf, leaves, legume, root, produce, seaweed, kelp, " \
                                "algae".split(", ")
        # keywords = self.water.keywords_to_subcategories
        # additional_keywords = []
        # for key in keywords.keys():
        #     if keywords.get(key) not in self.keywords:
        #         additional_keywords = additional_keywords + keywords.get(key)
        self.theme_keywords_not = "human, children, infant, adult, student, doctor, nurse, dentist, pharmacist, " \
                                  "patient, resident, hospital, ICU, long-term, clinic, clinician, health-care, " \
                                  "healthcare, health, facility, physician, probiotic, husbandry, veterinary, " \
                                  "zoonotic, zoonoses, zoonosis, CAFO, concentrated, feeding, operation, confined, " \
                                  "excreta, excrement, animal, livestock, poultry, bird, rabbit, pig, cow, bovine, " \
                                  "ovine, lamb, fish, chicken, piglet, shrimp, oyster, pet, companion, canine, " \
                                  "feline, cats, dogs, feces, cattle, wildlife, boar, broiler, mammals, " \
                                  "horses".split(", ")


if __name__ == "__main__":
    a = Plants()
    a.set_all_papers_primary_database()
    papers = a.all_papers
    print(len(papers))
    i = 0
    for paper in papers:
        if i == 10:
            break
        i = i + 1
        print(paper)
    # papers = a.get_papers_on_prevention()
    # print(len(papers))
    # papers = a.get_papers_on_surveillance()
    # print(len(papers))
    # papers = a.get_papers_on_mitigation()
    # print(len(papers))
    # papers = a.get_papers_on_innovation()
    # print(len(papers))
