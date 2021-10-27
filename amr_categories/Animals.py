from amr_categories.Themes import Themes
from amr_categories.Water import Water


class Animals(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "animals"
        self.water = Water()
        self.keywords = "antibiotic, antimicrobial, antibacterial, antibiotics, antimicrobials, antibacterials, " \
                        "anti-biotic, anti-microbial, anti-bacterial, multidrug resistance, multi-drug resistance, " \
                        "pan-drug, pandrug, use, usage, consumption, overuse, misuse, treatment, susceptibility, " \
                        "dosage, immunization, vaccination, vaccine, vaccines, probiotic, farm, aquaculture, " \
                        "husbandry, veterinary, zoonotics, zoonoses, zoonosis, CAFO, concentrated animal feeding " \
                        "operation, confined animal feeding operation, manure, manures, excreta, excrement".split(", ")
        self.keywords_and = "animal, animals, livestock, poultry, bird, birds, rabbit, rabbits, pig, pigs, cow, cows, " \
                            "pork, beef, bovine, ovine, lamb, " \
                            "dairy, mutton, fish, fishes, seafood, chicken, chickens, piglet, " \
                            "piglets, shrimp, shrimps, oyster, oysters, pet, pets, companion animal, " \
                            "companion animals, canine, feline".split(", ")
        self.theme_keywords = "use, usage, consumption, consume, prescribe, overuse, misuse, treatment, dosage, " \
                              "access, practice, prescription, stewardship, immunization, vaccine, behaviour, " \
                              "behavior".split(", ")
        self.general_keywords = "probiotic, farm, farmland, aquaculture, aquacultural, husbandry, veterinary, " \
                                "zoonotic, zoonoses, zoonosis, CAFO, concentrated, feeding, operation, confined, " \
                                "manure, excreta, excrement, animal, livestock, poultry, bird, rabbit, pig, cow, " \
                                "bovine, ovine, lamb, fish, chicken, piglet, shrimp, oyster, pet, companion, canine, " \
                                "feline, cats, dogs, feces, cattle, wildlife, wild, boar, broiler, mammals, " \
                                "horses".split(", ")
        self.theme_keywords_not = "human, children, infant, adult, student, doctor, nurse, dentist, pharmacist, " \
                                  "patient, resident, hospital, ICU, long-term, clinic, clinician, health-care, " \
                                  "healthcare, health, facility, physician, pesticide, herbicide, fungicide, biocide, " \
                                  "fertilizer, manure, agriculture, agricultural, pond, tank, nursery, horticulture, " \
                                  "harvest, plant, fruit, vegetable, crop, leaf, leaves, legume, root, produce, " \
                                  "seaweed, kelp, algae".split(", ")


if __name__ == "__main__":
    a = Animals()
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
