from amr_categories.Themes import Themes


class Animals(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "animals"
        self.keywords = "antibiotic, antimicrobial, antibacterial, antibiotics, antimicrobials, antibacterials, " \
                        "anti-biotic, anti-microbial, anti-bacterial, multidrug resistance, multi-drug resistance, " \
                        "pan-drug, pandrug, use, usage, consumption, overuse, misuse, treatment, susceptibility, " \
                        "dosage, immunization, vaccination, vaccine, vaccines, probiotic, farm, aquaculture, " \
                        "husbandry, veterinary, zoonotics, zoonoses, zoonosis, CAFO, concentrated animal feeding " \
                        "operation, confined animal feeding operation, manure, manures, excreta, excrement".split(", ")
        self.keywords_and = "animal, animals, livestock, poultry, bird, birds, rabbit, rabbits, pig, pigs, cow, cows, " \
                            "pork, beef, bovine, dairy, mutton, fish, fishes, seafood, chicken, chickens, piglet, " \
                            "piglets, shrimp, shrimps, oyster, oysters, pet, pets, companion animal, " \
                            "companion animals, canine, feline".split(", ")


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
