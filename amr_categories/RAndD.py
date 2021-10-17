from amr_categories.Themes import Themes


class RAndD(Themes):
    def __init__(self):
        super().__init__()
        self.theme = 'randd'
        self.keywords = "antibiotic, antimicrobial, antibacterial, antibiotics, antimicrobials, antibacterials, " \
                        "anti-biotic, anti-microbial, anti-bacterial, anti-biotics, anti-microbials, anti-bacterials, " \
                        "multidrug, multidrugs, multi-drug, multi-drugs, drug, drugs, vaccine, vaccines, therapeutic, " \
                        "therapeutics, gene, genes, genome, genomic, genomics, peptide, peptides, plasmid, plasmids, " \
                        "serotype, serotypes, serotyped, serovar, serovars, pathogen, pathogens, carbapenem, " \
                        "carbapenems, biofilm, biofilms, efflux pump, efflux pumps".split(", ")
        self.keywords_and = "research and development, R&D, development, genesis, evolution, sequence, sequencing, " \
                            "nanotechnology-based, trend, trends, modelling, model, models, review, scoping review, " \
                            "study, detect, detects, detected, detection, diagnostic, diagnostics, mutation, " \
                            "mutations, alternative, agent, agents, susceptibility, activity, activities, activation, " \
                            "activate, activator, activators, deactivate, deactivation, deactivator, deactivators, " \
                            "inactivation, inactivate, mechanism, mechanisms".split(", ")
        self.prevention = "defence, peptide, peptides, drug, drugs, vaccine, vaccines".split(", ") + self.prevention
        self.prevention = list(dict.fromkeys(self.prevention))

        self.r_and_d = "gene identification, peptide, peptides, efflux pump, efflux pumps, biofilm, biofilms, " \
                       "inactivation, deactivation, identification".split(", ") + self.r_and_d
        self.r_and_d = list(dict.fromkeys(self.r_and_d))
        self.theme_keywords = "research, development, R&D, genesis, evolution, sequence, nanotechnology-based, trend, " \
                              "model, review, scope, study, detect, diagnostic, mutation, alternative, agent, " \
                              "susceptibility, activity, activation, activate, activator, deactivate, deactivation, " \
                              "deactivator, inactivation, inactivate, mechanism, gene, genome, genomic, peptide, " \
                              "plasmid, serotype, serovar, pathogen, carbapenem, biofilm, efflux, " \
                              "pump, antibiotic, antimicrobial, antibacterial, anti-biotic, anti-microbial, " \
                              "anti-bacterial, multidrug, multi-drug, drug, vaccine, therapeutic".split(", ")
        self.theme_keywords_not = "use, usage, consumption, consume, prescribe, overuse, misuse, access, " \
                                  "over-the-counter, duration, treatment, dosage, practice, prescription, " \
                                  "stewardship, immunization, vaccine, behaviour, behavior, practice".split(", ")


if __name__ == "__main__":
    a = RAndD()
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
