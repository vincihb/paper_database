from amr_categories.Animals import Animals
from amr_categories.CleanWater import CleanWater
from amr_categories.Environment import Environment
from amr_categories.FoodSafety import FoodSafety
from amr_categories.HumanConsumption import HumanConsumption
from amr_categories.HumanIPC import HumanIPC
from amr_categories.Plants import Plants
from amr_categories.RAndD import RAndD
from data.PaperCache import PaperCache
from regression.Linear import Linear
import numpy as np
import matplotlib.pyplot as plt

# Data Here
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
a.set_all_papers_primary_database()
b = CleanWater()
b.set_all_papers_primary_database()
c = Environment()
c.set_all_papers_primary_database()
d = FoodSafety()
d.set_all_papers_primary_database()
e = HumanConsumption()
e.set_all_papers_primary_database()
f = HumanIPC()
f.set_all_papers_primary_database()
g = Plants()
g.set_all_papers_primary_database()
h = RAndD()
h.set_all_papers_primary_database()

for year in years:
    animal.append(len(a.get_papers_by_year(year)))
    cleanwater.append(len(b.get_papers_by_year(year)))
    environment.append(len(c.get_papers_by_year(year)))
    foodsafety.append(len(d.get_papers_by_year(year)))
    human_consumption.append(len(e.get_papers_by_year(year)))
    human_ipc.append(len(f.get_papers_by_year(year)))
    plants.append(len(g.get_papers_by_year(year)))
    rd.append(len(h.get_papers_by_year(year)))

labels = "Animals, Clean Water, Environment, Food Safety, Human Consumption, Human IPC, Plants, R and D".split(", ")
yearly_data = [animal, cleanwater, environment, foodsafety, human_consumption, human_ipc, plants, rd]
vals = [sum(a) for a in yearly_data]

# Plotting data over the years
plt.plot(years, animal, label="Animals")
plt.plot(years, cleanwater, label="Clean Water")
plt.plot(years, environment, label="Environment")
plt.plot(years, foodsafety, label="Food Safety")
plt.plot(years, human_consumption, label="Human Consumption")
plt.plot(years, human_ipc, label="Human IPC")
plt.plot(years, plants, label="Plants")
plt.plot(years, rd, label="R and D")
plt.grid()
plt.legend()
# plt.show()
plt.xlabel("Year")
plt.ylabel("Number of papers")
plt.tight_layout()
plt.savefig("images/trends_over_time/trends")
plt.close()

index = 0
for data in yearly_data:
    print("=====")
    print(labels[index])
    plt.plot(years, np.log(data + np.ones_like(data)), label=labels[index])
    m, intercept, r, x_hat, y_hat = Linear(years, np.log(data + np.ones_like(data))).get_all_data()
    plt.plot(x_hat, y_hat, label="Linear regression R squared value " + str(round(r, 5)))
    print("Slope is " + str(m))
    print("Intercept is " + str(intercept))
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Log number of papers")
    plt.tight_layout()
    plt.savefig("images/log_trends/log_trends_" + labels[index].lower().replace(" ", "_"))
    plt.close()
    index += 1

animal = []
cleanwater = []
environment = []
foodsafety = []
human_consumption = []
human_ipc = []
plants = []
rd = []
for year in range(2000, 2010):
    animal.append(len(a.get_papers_by_year(year)))
    cleanwater.append(len(b.get_papers_by_year(year)))
    environment.append(len(c.get_papers_by_year(year)))
    foodsafety.append(len(d.get_papers_by_year(year)))
    human_consumption.append(len(e.get_papers_by_year(year)))
    human_ipc.append(len(f.get_papers_by_year(year)))
    plants.append(len(g.get_papers_by_year(year)))
    rd.append(len(h.get_papers_by_year(year)))

fig = plt.figure(figsize=(15, 5))
# print(vals)
plt.bar(labels, vals)
plt.xlabel("Theme")
plt.ylabel("Number of papers from 2000 to 2009")
plt.tight_layout()
plt.savefig("images/trends_over_time/trends_2000")

classes = [a, b, c, d, e, f, g, h]
changes = {label: [] for label in classes}
for year in range(1990, 2020, 1):
    for cl in classes:
        try:
            # change = np.log(len(cl.get_papers_by_year(year)) + 0.01)
            change = (len(cl.get_papers_by_year(year))
                      - len(cl.get_papers_by_year(year - 1))) \
                # /float(len(cl.get_papers_by_year(year - 1)))
        except ZeroDivisionError:
            print(cl.theme)
            change = len(cl.get_papers_by_year(year))
        changes.get(cl).append(change)
# print(changes)
results = {cl.theme: [np.mean(changes.get(cl)), np.var(changes.get(cl))] for cl in changes.keys()}
# print(results)
results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
print(results)
