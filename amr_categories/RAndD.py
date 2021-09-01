from amr_categories.Themes import Themes


class RAndD(Themes):
    def __init__(self):
        super().__init__()
        self.keywords = "discovery, laboratory, novel, therapeutic, new antibiotics, R&D, new diagnostics, " \
                        "drug development, drugs development, vaccine development, clinical trial, alternative " \
                        "medicine, alternative antibiotics, alternative antimicrobials, peptide, peptides, " \
                        "drug resistance, drugs resistance, defence, screening, synthesized derivatives, " \
                        "susceptibility testing, sensitivity, antibiotic susceptibility, sequence, sequencing, " \
                        "detection of antibiotic resistance, detection of antimicrobial resistance, identification of " \
                        "antimicrobial resistance, identification of antibiotic resistance, resistant gene, " \
                        "resistant genes, resistance gene, resistance genes, pathogen, pathogens, mutation, " \
                        "mutations, genesis, emergence, evolution, test, testing, biofilm, biofilms, error rate, " \
                        "error rates, activation, activate, deactivate, deactivation".split(", ")
        self.prevention = "prevention, education, awareness, training, defence, peptide, peptides, drug, drugs, " \
                          "vaccine, vaccines".split(", ") + self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))

        self.r_and_d = "discovery, laboratory, novel, therapeutic, innovation, innovative, new antibiotics, R&D, " \
                       "new diagnostics, accelerator, method development, tool development, drug development, " \
                       "vaccine development, clinical trial, funding, pilot, translational, biomedicine, de novo, " \
                       "alternative medicine, alternative antibiotics, gene identification, peptide, peptides, " \
                       "biofilm, biofilms, inactivation, deactivation, identification, technology, technological, " \
                       "sequence, error rates".split(", ") + self.r_and_d
        self.r_and_d = list(dict.fromkeys(self.r_and_d))

        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = RAndD()
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
