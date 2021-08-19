from data.PaperCache import PaperCache
from amr_categories.Water import Water
from nltk import word_tokenize
from nltk.corpus import stopwords


class Themes:
    def __init__(self):
        self.pc = PaperCache()
        self.water = Water()
        self.human_ipc = "Infection Prevention and Control, hygiene, hand hygiene, personal protective equipment, " \
                         "PPE, disinfection, sterilization, safe disposal, environmental cleaning, isolation, " \
                         "waste management, sanitation, surfaces, " \
                         "stewardship, hospital, clinical, health care " \
                         "facility"
        self.human_ipc = self.human_ipc.split(", ")
        self.human_consumption = "consumption, antibiotic overuse, antibiotic prescribing, antibiotic use, " \
                                 "antibiotic, access, over the counter, antibiotic misuse, dosage, treatment duration, " \
                                 "daily dose, prescribing practices, stewardship,  hospital, clinical, health care " \
                                 "healthcare, facility, doctor, nurse, pharmacist"
        self.human_consumption = self.human_consumption.split(", ")
        self.r_and_d = "discovery, laboratory, novel, therapeutic, research, innovation, innovative, " \
                       "new antimicrobials, R&D, new diagnostics, new classes of medication, accelerator, " \
                       "method development, tool development, drug development, vaccine development, clinical trial, " \
                       "push funding, pull funding, in vitro, pipeline, pilot, translational, biomedicine, de novo, " \
                       "database, alternative medicine, complementary medicine"
        self.r_and_d = self.r_and_d.split(", ")
        self.clean_water = "clean water, sanitation, hygiene, WASH, water supply, water intervention, " \
                           "leaching, leachate, " \
                           "water reservoir, wastewater, effluent, fecal matter, water treatment, filtration, " \
                           "chlorination, removal"
        self.clean_water = self.clean_water.split(", ")
        keywords = self.water.keywords_to_subcategories
        additional_keywords = []
        for key in keywords.keys():
            if keywords.get(key) not in self.clean_water:
                additional_keywords = additional_keywords + keywords.get(key)
        self.clean_water = self.clean_water + additional_keywords
        self.clean_water = list(dict.fromkeys(self.clean_water))
        self.environment = "environmental contamination, environmental AMR, pollution source, water, soil, " \
                           "transmission vector, selective pressure, reservoir, resistance development, " \
                           "source of resistance, antibiotic concentration, run-off, wildlife, manures, ecology, " \
                           "ecosystem, remediation, environmental DNA, eDNA"
        self.environment = self.environment.split(", ")
        self.food_safety = "food supply, supply of food, food safety, food security, food handling, street food, " \
                           "food contamination, food processing, food production, food retail, supply chain, " \
                           "food import, industrial hygiene, food systems, grocery, food packaging, foodborne, " \
                           "food-borne"
        self.food_safety = self.food_safety.split(", ")
        self.animals = "Animals, farm animals, food producing animals, poultry, birds, pigs, cows, poultry, " \
                       "livestock, veterinary, companion animals, husbandary, aquaculture, ruminants, probiotics, " \
                       "zoonoses, zoonosis, zoonotic, pets, canine, feline, " \
                       "CAFO, swine, beef, dairy, mutton, pork, fish, seafood, manures"
        self.animals = self.animals.split(", ")
        self.plants = "pesticides, " \
                      "herbicides, fungicides, fertilizers, tree, trees, agriculture, soil, " \
                      "plants NOT wastewater, plant NOT wastewater, aquaculture, food produce, fruit, vegetable, " \
                      "harvest, crop, food, horticulture, nursery, orchard, biocide, farm, leaf, leaves, legume, " \
                      "roots, manures, horticulture, botany"
        self.plants = self.plants.split(", ")

    def get_human_ipc_papers(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.human_ipc)
        to_return = []
        for paper in papers:
            for keyword in self.human_ipc:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_human_consumption_papers(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.human_consumption)
        to_return = []
        for paper in papers:
            for keyword in self.human_consumption:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_r_and_d(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.r_and_d)
        to_return = []
        for paper in papers:
            for keyword in self.r_and_d:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_clean_water(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.clean_water)
        to_return = []
        for paper in papers:
            for keyword in self.clean_water:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_environment(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.environment)
        to_return = []
        for paper in papers:
            for keyword in self.environment:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_food_safety(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.food_safety)
        to_return = []
        for paper in papers:
            for keyword in self.food_safety:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_animals(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.animals)
        to_return = []
        for paper in papers:
            for keyword in self.animals:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return

    def get_plants(self):
        papers = self.pc.get_papers_from_list_of_keywords_or(self.plants)
        to_return = []
        for paper in papers:
            for keyword in self.plants:
                if keyword in paper.get("TITLE"):
                    to_return.append(paper)
                    break
        return to_return


if __name__ == "__main__":
    a = Themes()
    papers = a.get_clean_water()
    print(a.clean_water)
    print(len(papers))
    i = 0
    for paper in papers:
        if i == 10:
            break
        i = i + 1
        print(paper)
    for paper in papers:
        if paper.get("DOI") == '10.1186/1471-2458-10-414':
            print(paper)
            break

    # pc = PaperCache()
    # papers = pc.get_papers_from_list_of_keywords_or(["Columbia", "British Columbia"])
    # print(len(papers))
    # i = 0
    # for paper in papers:
    #     print(paper)
    #     # if i == 10:
    #     #     break
    #     i = i + 1
    #
    # papers = pc.get_papers_from_keyword("Columbia")
    # print(len(papers))
    # i = 0
    # for paper in papers:
    #     print(paper)
    #     # if i == 10:
    #     #     break
    #     i = i + 1
    #
    # papers = pc.get_papers_from_keyword("British Columbia")
    # print(len(papers))
    # i = 0
    # for paper in papers:
    #     print(paper)
    #     # if i == 10:
    #     #     break
    #     i = i + 1
