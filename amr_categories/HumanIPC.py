from amr_categories.Themes import Themes


class HumanIPC(Themes):
    def __init__(self):
        super().__init__()
        self.theme = "ipc"
        self.keywords = "infection, prevention, control, surface, hygiene, personal " \
                        "protective equipment, PPE, disinfection, sterilization, sanitization, hand washing, " \
                        "mask wearing".split(", ")
        self.keywords_and = "human, humans, clinical, clinic, clinics, hospital, hospitals".split(", ")
        self.theme_keywords = "infection, prevention, control, personal, protective, equipment, PPE, disinfection, " \
                              "sterilization, sanitization, washing, mask, " \
                              "human, children, infant, adult, student, doctor, nurse, dentist, pharmacist, " \
                              "patient, resident, hospital, long-term, clinic, clinician, health-care, healthcare, " \
                              "health, facility, surface, hygiene".split(", ")
        self.theme_keywords_not = "use, usage, consumption, consume, prescribe, overuse, misuse, access, dosage, " \
                                  "practice, prescription, stewardship, immunization, vaccine, behaviour, behavior, " \
                                  "supply, safety, security, production, supply, chain, handling, processing, " \
                                  "slaughter, butcher, butchery, packaging, import, export, retail, street, grocery, " \
                                  "food, foodborne, food-borne".split(", ")
        self.prevention = "personal protective equipment, PPE, disinfection, sterilization, sanitization, " \
                          "hand washing, mask wearing, hospital surface, clinical surface".split(", ") + self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))
        self.mitigation = "infection control".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))


if __name__ == "__main__":
    a = HumanIPC()
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
