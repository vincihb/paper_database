from amr_categories.Themes import Themes


class Animals(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "usage of antimicrobials in animals, use of antimicrobials in animals, " \
                        "farm animals, food producing animals, " \
                        "poultry, bird, pig, pigs, cow, cows, antibiotics in animals, livestock, veterinary, " \
                        "companion animals, husbandary, ruminants, probiotic, zoonosis, zoonoses, zoonotic, pets, " \
                        "canine, feline, pork, beef, bovine, dairy, mutton, fish, fishes, seafood, chicken, manures, " \
                        "manure, CAFO, aquaculture animals, piglets, shrimp, shrimps"
        self.keywords = self.keywords.split(", ")
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = Animals()
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
