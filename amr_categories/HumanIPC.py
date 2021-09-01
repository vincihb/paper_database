from amr_categories.Themes import Themes


class HumanIPC(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "human infection, infection prevention, infection control, hospital surface, clinical " \
                        "surface, hand hygiene, hospital infection, personal protective equipment, PPE, disinfection, " \
                        "sterilization, sanitization, hand washing, mask wearing, hospital stewardship".split(", ")
        self.prevention = "prevention, personal protective equipment, PPE, disinfection, sterilization, sanitization, " \
                          "hand washing, mask wearing, prescribing practice, prescribing practices, education, " \
                          "awareness, training".split(", ") + self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))
        self.mitigation = "mitigation, infection control, removal, treatment, treatments, policy, policies, " \
                          "regulation, regulations, standard, standards, reduction, protocol, protocols, guideline, " \
                          "guidelines, strategy, strategies, stewardship".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    ipc = HumanIPC()
    papers = ipc.get_all_papers()
    print(len(papers))
    papers = ipc.get_papers_on_prevention()
    print(len(papers))
    papers = ipc.get_papers_on_surveillance()
    print(len(papers))
    papers = ipc.get_papers_on_mitigation()
    print(len(papers))
    papers = ipc.get_papers_on_innovation()
    print(len(papers))
    # papers = ipc.get_papers_by_year(1996)
    # print(len(papers))

