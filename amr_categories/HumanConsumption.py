from amr_categories.Themes import Themes


class HumanConsumption(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "consumption, antibiotic consumption, antibiotic overuse, antibiotic prescribing, " \
                        "antibiotic use, antibiotic misuse, antibiotic access, over the counter, dosage, " \
                        "treatment duration, daily dosage, prescribing practice, hospital stewardship, " \
                        "prescribed, prescription, hospital, clinical, health care, healthcare, facility, " \
                        "doctor, nurse, pharmacist"
        self.prevention = "prevention, hospital stewardship, prescribing practice"
        self.surveillance = "surveillance, hospital, clinical, health care, " \
                            "healthcare, facility, doctor, nurse, pharmacist"
        self.mitigation = "mitigation, stewardship, antibiotic access, patient education"

        self.keywords = self.keywords.split(", ")
        self.prevention = self.prevention.split(", ")
        self.surveillance = self.surveillance.split(", ")
        self.mitigation = self.mitigation.split(", ")

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    consumption = HumanConsumption()
    papers = consumption.get_all_papers()
    print(len(papers))
    papers = consumption.get_papers_on_prevention()
    print(len(papers))
    papers = consumption.get_papers_on_surveillance()
    print(len(papers))
    papers = consumption.get_papers_on_mitigation()
    print(len(papers))
    papers = consumption.get_papers_on_innovation()
    print(len(papers))

