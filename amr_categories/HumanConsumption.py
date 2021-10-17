from amr_categories.Themes import Themes


class HumanConsumption(Themes):
    def __init__(self):
        super().__init__()
        self.theme = 'consumption'
        self.keywords = "antibiotic, antimicrobial, antibacterial, antibiotics, antimicrobials, antibacterials, " \
                        "anti-biotic, anti-microbial, anti-bacterial, multidrug resistance, multi-drug resistance, " \
                        "pan-drug, pandrug, use, usage, consumption, prescribing, overuse, misuse, access, " \
                        "over the counter, treatment duration, treatment, susceptibility, dosage, prescribing " \
                        "practice, prescribed, prescription, stewardship, immunization, vaccination, vaccine, " \
                        "vaccines, behaviour, behavior, practice, practices".split(", ")
        self.keywords_and = "human, humans, children, infants, adult, adults, doctor, doctors, nurse, nurses, " \
                            "dentist, dentists, pharmacist, pharmacists, patient, patients, resident, residents, " \
                            "self-medicate, self-medication, hospital, hospitals, long-term care, clinical, clinic, " \
                            "clinics, clinicians, health care, healthcare, facility".split(", ")
        self.theme_keywords = "use, usage, consumption, consume, prescribe, overuse, misuse, treatment, dosage, " \
                              "access, dosage, practice, prescription, stewardship, immunization, vaccine, behaviour," \
                              " behavior, human, children, infant, adult, " \
                              "student, doctor, nurse, dentist, pharmacist, " \
                              "patient, resident, hospital, long-term, clinic, clinician, health-care, healthcare, " \
                              "health, facility".split(", ")
        self.theme_keywords_not = "infection, prevention, control, personal, protective, equipment, PPE, " \
                                  "disinfection, sterilization, sanitization, washing, mask, probiotic, farm, " \
                                  "aquaculture, husbandry, veterinary, zoonotics, zoonoses, zoonosis, CAFO, " \
                                  "concentrated, feeding, operation, confined, manure, excreta, excrement, animal, " \
                                  "livestock, poultry, bird, rabbit, pig, cow, pork, beef, bovine, ovine, lamb, " \
                                  "dairy, mutton, fish, seafood, chicken, piglet, shrimp, oyster, pet, companion, " \
                                  "canine, feline, feces, pesticide, herbicide, fungicide, biocide, fertilizer, " \
                                  "manure, farm, agriculture, agricultural, aquaculture, pond, tank, nursery, " \
                                  "horticulture, harvest, plant, fruit, vegetable, crop, leaf, leaves, legume, root, " \
                                  "produce, seaweed, kelp, algae".split(", ")
        self.prevention = "stewardship, immunization, vaccination, vaccine, vaccines, " \
                          "behaviour, behavior, practice, practices".split(", ") + self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))
        self.surveillance = "hospital, hospitals, long-term care, clinical, clinic, clinics, health care, healthcare, " \
                            "facility".split(", ") + self.surveillance
        self.surveillance = list(dict.fromkeys(self.surveillance))
        self.mitigation = "rotational, rotation, cycle, cycling".split(", ") + self.mitigation
        self.mitigation = list(dict.fromkeys(self.mitigation))


if __name__ == "__main__":
    a = HumanConsumption()
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
