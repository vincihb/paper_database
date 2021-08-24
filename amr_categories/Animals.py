from amr_categories.Themes import Themes


class Animals(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "farm animals, food producing animals, poultry, bird, pig, cow, " \
                        "antibiotics in animals, livestock, veterinary, companion animals, husbandary, " \
                        "ruminants, probiotic, zoonosis, zoonoses, zoonotic, pets, canine, feline, beef farm, " \
                        "dairy, pork, mutton, fish, seafood, chicken, manures, manure, CAFO"
        self.prevention = "prevention"
        self.surveillance = "surveillance"
        self.mitigation = "mitigation, sanitization, pasteurization"

        self.keywords = self.keywords.split(", ")
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")

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
