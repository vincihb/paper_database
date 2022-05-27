import random
from amr_categories.Animals import Animals
from amr_categories.CleanWater import CleanWater
from amr_categories.Environment import Environment
from amr_categories.FoodSafety import FoodSafety
from amr_categories.HumanConsumption import HumanConsumption
from amr_categories.HumanIPC import HumanIPC
from amr_categories.Plants import Plants
from amr_categories.RAndD import RAndD
from data.PaperCache import PaperCache

themes = {Animals().theme: Animals(), CleanWater().theme: CleanWater(),
          Environment().theme: Environment(), FoodSafety().theme: FoodSafety(),
          HumanConsumption().theme: HumanConsumption(), HumanIPC().theme: HumanIPC(),
          Plants().theme: Plants(), RAndD().theme: RAndD()}
for theme in themes.keys():
    themes.get(theme).set_all_papers_primary_database()
pillar_papers = {theme: {'prevention': [paper.get('ID') for paper in themes.get(theme).get_papers_on_prevention()],
                         'surveillance': [paper.get('ID') for paper in themes.get(theme).get_papers_on_surveillance()],
                         'mitigation': [paper.get('ID') for paper in themes.get(theme).get_papers_on_mitigation()],
                         'innovation': [paper.get('ID') for paper in themes.get(theme).get_papers_on_innovation()]} for
                 theme in themes.keys()}
a = PaperCache()
# a.set_all_papers_primary_database()
papers = a.get_all_papers()
n = (1.96 / 0.05) ** 2 * 0.25
sample_size = (len(papers) * n) / (len(papers) + n)
print("Sample size: " + str(round(sample_size, 0)))
print("Total: " + str(len(papers)))
sample = random.sample(papers, 373)
accuracy_array = []
pillar_accuracy_array = []
index = 0
for s in sample:
    print(index)
    index = index + 1
    print(s.get('TITLE'))
    print(s.get('ABSTRACT'))
    print("Primary theme is: " + a.get_paper_theme(s.get('ID'))[0].get('PRIMARY_THEME'))
    print("Secondary theme is: " + a.get_paper_theme(s.get('ID'))[0].get('SECONDARY_THEME'))
    pillar_val = {
        'prevention': s.get('ID') in pillar_papers.get(a.get_paper_theme(s.get('ID'))[0].get('PRIMARY_THEME')).get(
            'prevention'),
        'surveillance': s.get('ID') in pillar_papers.get(a.get_paper_theme(s.get('ID'))[0].get('PRIMARY_THEME')).get(
            'surveillance'),
        'mitigation': s.get('ID') in pillar_papers.get(a.get_paper_theme(s.get('ID'))[0].get('PRIMARY_THEME')).get(
            'mitigation'),
        'innovation': s.get('ID') in pillar_papers.get(a.get_paper_theme(s.get('ID'))[0].get('PRIMARY_THEME')).get(
            'innovation')
    }
    print(pillar_val)
    # while True:
    #     try:
    #         accuracy_array.append(int(input("Correctly identified primary and secondary themes? ")))
    #         break
    #     except ValueError:
    #         print("Please enter integer 0, 1: ")
    #         print("Accuracy estimate: " + str(sum(accuracy_array) / len(accuracy_array)))
    while True:
        try:
            pillar_accuracy_array.append(int(input("Correctly identified pillars? ")))
            break
        except ValueError:
            print("Please enter integer 0, 1: ")
            print("Pillar Accuracy estimate: " + str(sum(pillar_accuracy_array) / len(pillar_accuracy_array)))
# print("Accuracy estimate: " + str(sum(accuracy_array) / len(accuracy_array)))
print("Pillar Accuracy estimate: " + str(sum(pillar_accuracy_array) / len(pillar_accuracy_array)))
# print("====")
# print("Secondary Theme papers sample")
# accuracy_array = []
# a.set_all_papers_secondary_database()
# papers = a.all_papers
# sample = random.sample(papers, 94)
# print("Total: " + str(len(papers)))
# for s in sample:
#     print(s.get('TITLE'))
#     print(s.get('ABSTRACT'))
#     while True:
#         try:
#             accuracy_array.append(int(input("Secondary theme? ")))
#             break
#         except ValueError:
#             print("Please enter integer 0, 1: ")
#             print("Accuracy estimate: " + str(sum(accuracy_array) / len(accuracy_array)))
