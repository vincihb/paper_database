from amr_categories.Animals import Animals
from amr_categories.CleanWater import CleanWater
from amr_categories.Environment import Environment
from amr_categories.FoodSafety import FoodSafety
from amr_categories.HumanConsumption import HumanConsumption
from amr_categories.HumanIPC import HumanIPC
from amr_categories.Plants import Plants
from amr_categories.RAndD import RAndD
from data.PaperCache import PaperCache
from amr_categories.Water import Water
from countries.income.HIC import HIC
from countries.income.UMIC import UMIC
from countries.income.LMIC import LMIC
from countries.income.LDC import LDC
from countries.regions import Africa
from countries.regions import Caribbean
from countries.regions import EastAsia
from countries.regions import Europe
from countries.regions import MiddleEast
from countries.regions import NorthAmerica
from countries.regions import SouthAsia
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

labels = "Human IPC, Clean Water, Food Safety, Environment, Human Consumption, Animal, Plants, R and D".split(", ")
yearly_data = [human_ipc, cleanwater, foodsafety, environment, human_consumption, animal, plants, rd]
vals = [sum(a_vals) for a_vals in yearly_data]

# Bar plot of themes
fig = plt.figure(figsize=(15, 5))
plt.xticks(range(len(vals)), labels)
plt.xlabel('Themes')
plt.ylabel('Number of papers')
plt.bar(range(len(vals)), vals)
plt.tight_layout()
plt.savefig("images/bar_graphs/themes")
plt.close()

# Plotting data over the years
i = 0
while i < len(yearly_data):
    plt.plot(years, yearly_data[i], label=labels[i])
    i += 1
plt.grid()
# plt.plot(years, animal, label="Animals")
# plt.plot(years, cleanwater, label="Clean Water")
# plt.plot(years, environment, label="Environment")
# plt.plot(years, foodsafety, label="Food Safety")
# plt.plot(years, human_consumption, label="Human Consumption")
# plt.plot(years, human_ipc, label="Human IPC")
# plt.plot(years, plants, label="Plants")
# plt.plot(years, rd, label="R and D")
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
    print(data)
    plt.plot(years, np.log([value + np.exp(-1 / 2.0) if value == 0 else value for value in data]), label=labels[index])
    m, intercept, r, x_hat, y_hat = Linear(years, np.log(
        [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])).get_all_data()
    plt.plot(x_hat, [y if y >= 0 else y for y in y_hat],
             label="Linear regression for R squared value " + str(round(r, 5)))
    print(str(round(r, 4)))
    print("Slope is " + str(round(m, 4)))
    print("Intercept is " + str(round(intercept, 4)))
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
plt.close()

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

trends_regions = {'East Asia & Pacific': [], 'Europe & Central Asia': [], 'Latin America & Caribbean': [],
                  'Middle East & North Africa': [], 'North America': [], 'South Asia': [], 'Sub-Saharan Africa': []}
africa = Africa.Africa()
car = Caribbean.Caribbean()
east_asia = EastAsia.EastAsia()
europe = Europe.Europe()
middle_east = MiddleEast.MiddleEast()
north_america = NorthAmerica.NorthAmerica()
south_asia = SouthAsia.SouthAsia()
regions_classes = {'Sub-Saharan Africa': africa, 'Latin America & Caribbean': car,
                   'East Asia & Pacific': east_asia, 'Europe & Central Asia': europe,
                   'Middle East & North Africa': middle_east, 'North America': north_america, 'South Asia': south_asia}
for key in regions_classes.keys():
    for year in range(1990, 2021):
        trends_regions.get(key).append(len(regions_classes.get(key).get_papers_by_year(year)))
print("Regions")
print(trends_regions)
print({key: len(regions_classes.get(key).all_papers) for key in regions_classes.keys()})
fig = plt.figure(figsize=(16, 5))
plt.xticks(range(len(trends_regions)), [key for key in trends_regions.keys()])
plt.xlabel('Country Regions')
plt.ylabel('Number of papers')
plt.bar(range(len(trends_regions)),
        [val for val in {key: len(regions_classes.get(key).all_papers) for key in regions_classes.keys()}.values()])
plt.tight_layout()
plt.savefig("images/bar_graphs/regions")
plt.close()

trends_countries = {'hic': [], 'umic': [], 'lmic': [], 'ldc': []}
hic = HIC()
umic = UMIC()
lmic = LMIC()
ldc = LDC()
countries_classes = {'hic': hic, 'umic': umic, 'lmic': lmic, 'ldc': ldc}
all_papers_countries = []
for key in countries_classes.keys():
    all_papers_countries = pc.get_papers_or_countries(all_papers_countries, countries_classes.get(key).all_papers)
    for year in range(1990, 2021):
        trends_countries.get(key).append(len(countries_classes.get(key).get_papers_by_year(year)))

print("Countries")
print(len(all_papers_countries))
print(trends_countries)
print({key: len(countries_classes.get(key).all_papers) for key in trends_countries.keys()})
plt.xticks(range(len(trends_countries)), [key.upper() for key in trends_countries.keys()])
plt.xlabel('Income classification')
plt.ylabel('Number of papers')
plt.bar(range(len(trends_countries)),
        [val for val in {key: len(countries_classes.get(key).all_papers) for key in trends_countries.keys()}.values()])
plt.tight_layout()
plt.savefig("images/bar_graphs/income")
plt.close()

for key in trends_countries.keys():
    plt.plot(range(1990, 2021), trends_countries.get(key), label=key.upper())
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Number of papers")
    plt.tight_layout()
    plt.savefig("images/trends_over_time/country_trends")

# w = Water()
# trends_water_code = {'green': [], 'blue': [], 'brown': []}
# water_codes = w.get_secondary_papers_from_watercode_partition()
# print(len(water_codes.get('green')))
# print(len(water_codes.get('blue')))
# print(len(water_codes.get('brown')))
# for key in water_codes.keys():
#     for year in range(1990, 2021):
#         trends_water_code.get(key).append(len(w.get_papers_by_year(water_codes.get(key), year)))
#
# print(trends_water_code)
#
# for key in water_codes.keys():
#     print(key)
#     plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label=key)
#     plt.grid()
#     plt.legend()
#     plt.xlabel("Year")
#     plt.ylabel("Number of papers")
#     plt.tight_layout()
#     plt.savefig("images/trends_over_time/secondary_water_code_trends")
# plt.close()
