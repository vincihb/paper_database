from amr_categories.Animals import Animals
from amr_categories.CleanWater import CleanWater
from amr_categories.Environment import Environment
from amr_categories.FoodSafety import FoodSafety
from amr_categories.HumanConsumption import HumanConsumption
from amr_categories.HumanIPC import HumanIPC
from amr_categories.Plants import Plants
from amr_categories.RAndD import RAndD
from data.PaperCache import PaperCache
import matplotlib.pyplot as plt


years = [year for year in range(1990, 2021)]
animal = []
cleanwater = []
environment = []
foodsafety = []
human_consumption = []
human_ipc = []
plants = []
rd = []
pc = PaperCache()
# print(pc.get_all_journals())

a = Animals()
a.set_all_papers()
papers = a.all_papers
total_papers = papers
b = CleanWater()
b.set_all_papers()
papers = b.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)
c = Environment()
c.set_all_papers()
papers = c.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)
d = FoodSafety()
d.set_all_papers()
papers = d.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)
e = HumanConsumption()
e.set_all_papers()
papers = e.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)
f = HumanIPC()
f.set_all_papers()
papers = f.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)
g = Plants()
g.set_all_papers()
papers = g.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)
h = RAndD()
h.set_all_papers()
papers = h.all_papers
total_papers = pc.get_papers_ored_by_id(total_papers, papers)

print(len(total_papers))
all_papers = pc.get_all_papers()
print(len(all_papers))


remaining_papers = pc.get_papers_set_not(all_papers, total_papers)
print(len(remaining_papers))
i = 0
for paper in remaining_papers:
    if i == 100:
        break
    i = i + 1
    print(paper)

for year in years:
    animal.append(len(a.get_papers_by_year(year)))
    cleanwater.append(len(b.get_papers_by_year(year)))
    environment.append(len(c.get_papers_by_year(year)))
    foodsafety.append(len(d.get_papers_by_year(year)))
    human_consumption.append(len(e.get_papers_by_year(year)))
    human_ipc.append(len(f.get_papers_by_year(year)))
    plants.append(len(g.get_papers_by_year(year)))
    rd.append(len(h.get_papers_by_year(year)))

plt.plot(years, animal, label="Animals")
plt.plot(years, cleanwater, label="Clean Water")
plt.plot(years, environment, label="Environment")
plt.plot(years, foodsafety, label="Food Safety")
plt.plot(years, human_consumption, label="Human Consumption")
plt.plot(years, human_ipc, label="Human IPC")
plt.plot(years, plants, label="Plants")
plt.plot(years, rd, label="R and D")
plt.legend()
plt.show()


