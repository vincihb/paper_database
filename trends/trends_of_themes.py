from amr_categories.Animals import Animals
from amr_categories.CleanWater import CleanWater
from amr_categories.Environment import Environment
from amr_categories.FoodSafety import FoodSafety
from amr_categories.HumanConsumption import HumanConsumption
from amr_categories.HumanIPC import HumanIPC
from amr_categories.Plants import Plants
import matplotlib.pyplot as plt


years = [year for year in range(1980, 2021)]
animal = []
cleanwater = []
environment = []
foodsafety = []
human_consumption = []
human_ipc = []
plants = []
a = Animals()
b = CleanWater()
c = Environment()
d = FoodSafety()
e = HumanConsumption()
f = HumanIPC()
g = Plants()
for year in years:
    animal.append(len(a.get_papers_by_year(year)))
    cleanwater.append(len(b.get_papers_by_year(year)))
    environment.append(len(c.get_papers_by_year(year)))
    foodsafety.append(len(d.get_papers_by_year(year)))
    human_consumption.append(len(e.get_papers_by_year(year)))
    human_ipc.append(len(f.get_papers_by_year(year)))
    plants.append(len(g.get_papers_by_year(year)))

plt.plot(years, animal, label="Animals")
plt.plot(years, cleanwater, label="Clean Water")
plt.plot(years, environment, label="Environment")
plt.plot(years, foodsafety, label="Food Safety")
plt.plot(years, human_consumption, label="Human Consumption")
plt.plot(years, human_ipc, label="Human IPC")
plt.plot(years, plants, label="Plants")
plt.legend()
plt.show()


