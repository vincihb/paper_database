from data.PaperCache import PaperCache
from amr_categories.Water import Water
from nltk import word_tokenize
from nltk.corpus import stopwords


class Themes:
    def __init__(self):
        self.pc = PaperCache()
        self.water = Water()
        self.human_ipc = ["hospital surface, clinical surface, hand hygiene",
                          "PPE, personal protective equipment, disinfection, "
                          "sterilization, sanitization, hand washing, mask wearing, stewardship"]
        i = 0
        while i < len(self.human_ipc):
            str_1 = self.human_ipc[i]
            self.human_ipc[i] = str_1.split(", ")
            i = i + 1
        print(self.human_ipc)

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

        self.clean_water = ["leach, leaching, lechate, wastewater, effluent, "
                            "surface water, river, lake, stream, marine water, groundwater, influent",
                            "water treatment, wastewater treatment"
                            "water filtration, wastewater filteration,"
                            "chlorination, ultraviolet, UV light, oxidation, WASH"]

        i = 0
        while i < len(self.clean_water):
            str_1 = self.clean_water[i]
            self.clean_water[i] = str_1.split(", ")
            i = i + 1
        print(self.clean_water)

        # self.clean_water = "clean water, sanitation, hygiene, WASH, water supply, water intervention, " \
        #                    "leaching, leachate, " \
        #                    "water reservoir, wastewater, effluent, fecal matter, water treatment, filtration, " \
        #                    "chlorination, removal"
        # self.clean_water = self.clean_water.split(", ")
        # keywords = self.water.keywords_to_subcategories
        # additional_keywords = []
        # for key in keywords.keys():
        #     if keywords.get(key) not in self.clean_water:
        #         additional_keywords = additional_keywords + keywords.get(key)
        # self.clean_water = self.clean_water + additional_keywords
        # self.clean_water = list(dict.fromkeys(self.clean_water))

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
        result_1 = self.pc.get_papers_from_list_of_keywords_or(self.human_ipc[0])
        result_2 = self.pc.get_papers_from_list_of_keywords_or(self.human_ipc[1])
        return result_1, result_2, self.pc.get_papers_and(result_1, result_2)

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
        result_1 = self.pc.get_papers_from_list_of_keywords_or(self.clean_water[0])
        result_2 = self.pc.get_papers_from_list_of_keywords_or(self.clean_water[1])
        return result_1, result_2, self.pc.get_papers_and(result_1, result_2)

    def get_environment(self):
        return self.pc.get_papers_from_list_of_keywords_or(self.environment)

    def get_food_safety(self):
        return self.pc.get_papers_from_list_of_keywords_or(self.food_safety)

    def get_animals(self):
        return self.pc.get_papers_from_list_of_keywords_or(self.animals)

    def get_plants(self):
        return self.pc.get_papers_from_list_of_keywords_or(self.plants)


if __name__ == "__main__":
    # a = Themes()
    # papers = a.get_human_ipc_papers()
    # print(a.clean_water)
    # print(len(papers))
    # i = 0
    # for paper in papers:
    #     if i == 10:
    #         break
    #     i = i + 1
    #     print(paper)
    # for paper in papers:
    #     if paper.get("DOI") == '10.1186/1471-2458-10-414':
    #         print(paper)
    #         break

    # a = Themes()
    # papers_d, papers_g, intersection_papers = a.get_human_ipc_papers()
    # print(len(papers_d))
    # print(len(papers_g))
    # print(len(intersection_papers))
    str_1 = "Infection Prevention and Control, hand hygiene, " \
            "personal protective equipment, PPE, disinfection, sterilization, waste management, " \
            "hospital surface, sanitization, antibiotic consumption, antibiotic overuse, antibiotic prescribing, " \
            "antibiotic use, antibiotic misuse, antibiotic access, prescribing practice, " \
            "stewardship, prescribed, prescription, discovery, laboratory, " \
            "novel, therapeutic, innovation, innovative, new antibiotics, R&D, new diagnostics, " \
            "accelerator, method development, tool development, drug development, vaccine development, " \
            "clinical trial, funding, in vitro, pilot, translational, biomedicine, de novo, alternative medicine, " \
            "alternative antibiotics, clean water, WASH, water supply, leach, leaching, leachate, " \
            "wastewater, effluent, surface water, river, lake, stream, marine water, " \
            "groundwater, water treatment, water filtration, chlorination, " \
            "environmental contamination, environmental AMR, pollution, source of resistance, " \
            "run-off, wildlife, ecology, ecosystem, remediation, soil contamination, " \
            "food supply, food safety, food security, food handling, food processing, street food, food contamination, " \
            "food production, food retail, food import, food export, food system, " \
            "grocery, food packaging, foodborne, food-borne, food borne" \
            "food surfaces, farm animals, food producing animals, poultry, " \
            "bird, pig, cow, antibiotics in animals, livestock, veterinary, companion animals, " \
            "husbandry, ruminants, probiotic, zoonosis, canine, feline, beef farm, dairy, pork, " \
            "mutton, fish, seafood, chicken, plants, agriculture, pesticides, herbicides, " \
            "fungicides, fertilizers, horticulture, botany, fruit, vegetable, harvest, " \
            "crop, nursery, biocide, leaf, legume, roots, fresh produce"
    str_1 = str_1.split(", ")
    print(str_1)
    pc = PaperCache()
    papers_1 = pc.get_papers_from_list_of_keywords_or(str_1)
    papers_2 = pc.get_all_papers()
    to_return = []
    for paper_2 in papers_2:
        match_found = False
        for paper_1 in papers_1:
            if paper_1.get("ID") == paper_2.get("ID"):
                match_found = True
                break
        if not match_found:
            to_return.append(paper_2)

    print(len(to_return))
    i = 0
    for paper in to_return:
        print(paper)
        if i == 50:
            break
        i = i + 1
    # papers = pc.get_papers_from_list_of_keywords_or(["nurse", "nurses"])
    # print(len(papers))
    # papers = pc.get_papers_from_list_of_keywords_or(["doctor", "doctors"])
    # print(len(papers))
    # papers = pc.get_papers_from_list_of_keywords_or(["pharmacist", "pharmacists"])
    # print(len(papers))
    # papers = pc.get_papers_from_keyword("WASH")
    # print(len(papers))
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
