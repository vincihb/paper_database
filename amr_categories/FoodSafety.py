from amr_categories.Themes import Themes


class FoodSafety(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "food supply, food supplies, food safety, food security, food handling, food processing, " \
                        "street food, food contamination, food production, food retail, food import, " \
                        "food imports, food exports, food export, food system, food systems, grocery, groceries " \
                        "food packaging, foodborne, food borne, food surfaces, " \
                        "supply chain, industrial hygiene".split(", ")
        self.prevention = "prevention, education, awareness, training, sanitization, pasteurization, prescribing " \
                          "practice, prescribing practices".split(", ") + \
                          self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))
        self.mitigation = "mitigation, sanitization, pasteurization, removal, treatment, treatments, policy, " \
                          "policies, regulation, regulations, standard, standards, reduction, protocol, protocols, " \
                          "guideline, guidelines, strategy, strategies, stewardship".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))

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
