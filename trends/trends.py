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
from scipy.stats import spearmanr

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

labels = "Human IPC, Clean water & sanitation, Food safety & security, Environmental contamination, " \
         "Human consumption of antimicrobials, Use of antimicrobials in animals, " \
         "Use of antimicrobials in plants, R&D".split(", ")
yearly_data = [human_ipc, cleanwater, foodsafety, environment, human_consumption, animal, plants, rd]
# print(animal[-2]/float(sum([thing[-2] for thing in yearly_data])))
# print(cleanwater[-2]/float(sum([thing[-2] for thing in yearly_data])))
vals = [sum(a_vals) for a_vals in yearly_data]

# Bar plot of themes
plt.rc('font', size=16)
fig = plt.figure(figsize=(15, 5), dpi=300)
labels.reverse()
plt.yticks(range(len(vals)), labels, fontsize=15)
plt.ylabel('Themes')
plt.xlabel('Number of article records')
vals.reverse()
plt.barh(range(len(vals)), vals)
plt.tight_layout()
plt.savefig("images/bar_graphs/themes")
plt.close()

# Plotting data over the years
labels.reverse()
plt.rc('font', size=10)
plt.figure(dpi=300)
i = 0
while i < len(yearly_data):
    plt.plot(years, yearly_data[i], label=labels[i])
    i += 1
plt.grid()
plt.legend()
plt.xlabel("Year")
plt.ylabel("Number of article records")
plt.tight_layout()
plt.savefig("images/trends_over_time/trends")
plt.close()

index = 0
pred_year = 2030
pred_val = {label: 0 for label in labels}
for data in yearly_data:
    print("=====")
    print(labels[index])
    print(data)
    plt.figure(dpi=300)
    plt.plot(years, np.log([value + np.exp(-1 / 2.0) if value == 0 else value for value in data]), label=labels[index])
    m, intercept, r, x_hat, y_hat = Linear(years, np.log(
        [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])).get_all_data()
    pred_val.update({labels[index]: int(np.exp(m*pred_year + intercept))})
    plt.plot(x_hat, [y if y >= 0 else y for y in y_hat],
             label="Linear regression, R squared value " + str(round(r, 5)))
    print(str(round(r, 4)))
    print(spearmanr(years, np.log(
        [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])))
    print("Slope is " + str(round(m, 4)))
    print("Intercept is " + str(round(intercept, 4)))
    print("Predicted start year " + str(round((-0.5 - intercept) / float(m), 0)))
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Log number of article records")
    plt.tight_layout()
    plt.savefig("images/log_trends/log_trends_" + labels[index].lower().replace(" ", "_"))
    plt.close()
    index += 1
print(pred_val)
print({key: pred_val.get(key)/sum(pred_val.values()) for key in pred_val.keys()})

# Region data
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
plt.rc('font', size=16)
fig = plt.figure(figsize=(16, 5), dpi=300)
plt.yticks(range(len(trends_regions)), [key for key in regions_classes.keys()], fontsize=15)
plt.ylabel('Country Regions')
plt.xlabel('Number of article records')
plt.barh(range(len(regions_classes)),
        [val for val in {key: len(regions_classes.get(key).all_papers) for key in regions_classes.keys()}.values()])
plt.tight_layout()
plt.savefig("images/bar_graphs/regions")
plt.close()

# Region trends
plt.rc('font', size=10)
plt.figure(dpi=300)
for key in trends_regions.keys():
    plt.plot(range(1990, 2021), trends_regions.get(key), label=key)
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Number of article records")
    plt.tight_layout()
    plt.savefig("images/trends_over_time/region_trends")
plt.close()

index = 0
alpha = -0.5
pred_val = {label: 0 for label in regions_classes.keys()}
plt.figure(dpi=300)
for key in trends_regions.keys():
    print("=====")
    data = trends_regions.get(key)
    print(key)
    print(data)
    plt.plot(years, np.log([value + np.exp(alpha) if value == 0 else value for value in data]), label=key)
    m, intercept, r, x_hat, y_hat = Linear(years, np.log(
        [value + np.exp(alpha) if value == 0 else value for value in data])).get_all_data()
    pred_val.update({key: int(np.exp(m * pred_year + intercept))})
    plt.plot(x_hat, [y if y >= 0 else y for y in y_hat],
             label="Linear regression, R squared value " + str(round(r, 5)))
    print(str(round(r, 4)))
    print(spearmanr(years, np.log(
        [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])))
    print("Slope is " + str(round(m, 4)))
    print("Intercept is " + str(round(intercept, 4)))
    print("Predicted start year " + str(round((-intercept) / float(m), 0)))
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Log number of article records")
    plt.tight_layout()
    plt.savefig("images/regions_log_trends/log_trends_" + key.lower().replace(" ", "_"))
    plt.close()
    index += 1
print(sum(pred_val.values()))
print(pred_val)

# Income level data
trends_countries = {'hic': [], 'umic': [], 'lmic': [], 'ldc': []}
hic = HIC()
umic = UMIC()
lmic = LMIC()
ldc = LDC()
countries_classes = {'hic': hic, 'umic': umic, 'lmic': lmic, 'ldc': ldc}
for key in countries_classes.keys():
    for year in range(1990, 2021):
        trends_countries.get(key).append(len(countries_classes.get(key).get_papers_by_year(year)))

# Country bar graph
print("Countries")
print(trends_countries)
print({key: len(countries_classes.get(key).all_papers) for key in trends_countries.keys()})
plt.figure(dpi=300)
plt.xticks(range(len(trends_countries)), [key.upper() for key in trends_countries.keys()])
plt.xlabel('Income classification')
plt.ylabel('Number of article records')
plt.bar(range(len(trends_countries)),
        [val for val in {key: len(countries_classes.get(key).all_papers) for key in trends_countries.keys()}.values()])
plt.tight_layout()
plt.savefig("images/bar_graphs/income")
plt.close()

# Country trends
plt.figure(dpi=300)
for key in trends_countries.keys():
    plt.plot(range(1990, 2021), trends_countries.get(key), label=key.upper())
plt.legend()
plt.xlabel("Year")
plt.ylabel("Number of article records")
plt.tight_layout()
plt.grid()
plt.savefig("images/trends_over_time/country_trends")
plt.close()

for key in trends_countries.keys():
    print("=====")
    data = trends_countries.get(key)
    print(key)
    print(data)
    plt.figure(dpi=300)
    plt.plot(years, np.log([value + np.exp(alpha) if value == 0 else value for value in data]), label=key.upper())
    m, intercept, r, x_hat, y_hat = Linear(years, np.log(
        [value + np.exp(alpha) if value == 0 else value for value in data])).get_all_data()
    plt.plot(x_hat, y_hat,
             label="Linear regression, R squared value " + str(round(r, 5)))
    print(str(round(r, 4)))
    print(spearmanr(years, np.log(
        [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])))
    print("Slope is " + str(round(m, 4)))
    print("Intercept is " + str(round(intercept, 4)))
    print("Predicted start year " + str(round((alpha - intercept)/float(m), 0)))
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Log number of article records")
    plt.tight_layout()
    plt.savefig("images/income_log_trends/log_trends_" + key.lower().replace(" ", "_"))
    plt.close()
    index += 1

# Water codes
print("+++++ Water Codes ++++++")
print('primary')
w = Water()
trends_water_code = {'green': [], 'blue': [], 'brown': []}
water_codes = w.get_primary_papers_from_watercode_partition()
print(len(water_codes.get('green')))
print(len(water_codes.get('blue')))
print(len(water_codes.get('brown')))
for key in water_codes.keys():
    for year in range(1990, 2021):
        trends_water_code.get(key).append(len(w.get_papers_by_year(water_codes.get(key), year)))

print(trends_water_code)

plt.figure(dpi=300)
for key in water_codes.keys():
    print(key)
    if key == 'green':
        plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label='Source')
    elif key == 'blue':
        plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label='Supply')
    else:
        plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label='Wastewater')
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Number of article records")
    plt.tight_layout()
    plt.savefig("images/trends_over_time/primary_water_code_trends")
plt.close()

# for key in trends_water_code.keys():
#     print("=====")
#     data = trends_water_code.get(key)
#     print(key)
#     print(data)
#     plt.plot(years, np.log([value + np.exp(alpha) if value == 0 else value for value in data]), label=key.upper())
#     m, intercept, r, x_hat, y_hat = Linear(years, np.log(
#         [value + np.exp(alpha) if value == 0 else value for value in data])).get_all_data()
#     plt.plot(x_hat, y_hat,
#              label="Linear regression, R squared value " + str(round(r, 5)))
#     print(str(round(r, 4)))
#     print(spearmanr(years, np.log(
#         [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])))
#     print("Slope is " + str(round(m, 4)))
#     print("Intercept is " + str(round(intercept, 4)))
#     print("Predicted start year " + str(round((alpha - intercept)/float(m), 0)))
#     plt.grid()
#     plt.legend()
#     plt.xlabel("Year")
#     plt.ylabel("Log number of article records")
#     plt.tight_layout()
#     plt.savefig("images/water_log_trends/log_trends_primary_" + key.lower().replace(" ", "_"))
#     plt.close()

print('secondary')

trends_water_code = {'green': [], 'blue': [], 'brown': []}
water_codes = w.get_secondary_papers_from_watercode_partition()
print(len(water_codes.get('green')))
print(len(water_codes.get('blue')))
print(len(water_codes.get('brown')))
for key in water_codes.keys():
    for year in range(1990, 2021):
        trends_water_code.get(key).append(len(w.get_papers_by_year(water_codes.get(key), year)))

print(trends_water_code)

# for key in regions_classes.keys():
#     print(key)
#     region = regions_classes.get(key)
#     for key_w in trends_water_code.keys():
#         print(key_w)
#         print(len(pc.get_papers_and_countries(water_codes.get(key_w), region.all_papers)))


plt.figure(dpi=300)
for key in water_codes.keys():
    print(key)
    if key == 'green':
        plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label='Source')
    elif key == 'blue':
        plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label='Supply')
    else:
        plt.plot(range(1990, 2021), trends_water_code.get(key), color=key, label='Wastewater')
    plt.grid()
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Number of article records")
    plt.tight_layout()
    plt.savefig("images/trends_over_time/secondary_water_code_trends")
plt.close()

# for key in trends_water_code.keys():
#     print("=====")
#     data = trends_water_code.get(key)
#     print(key)
#     print(data)
#     plt.plot(years, np.log([value + np.exp(alpha) if value == 0 else value for value in data]), label=key.upper())
#     m, intercept, r, x_hat, y_hat = Linear(years, np.log(
#         [value + np.exp(alpha) if value == 0 else value for value in data])).get_all_data()
#     plt.plot(x_hat, y_hat,
#              label="Linear regression, R squared value " + str(round(r, 5)))
#     print(str(round(r, 4)))
#     print(spearmanr(years, np.log(
#         [value + np.exp(-1 / 2.0) if value == 0 else value for value in data])))
#     print("Slope is " + str(round(m, 4)))
#     print("Intercept is " + str(round(intercept, 4)))
#     print("Predicted start year " + str(round((alpha - intercept)/float(m), 0)))
#     plt.grid()
#     plt.legend()
#     plt.xlabel("Year")
#     plt.ylabel("Log number of article records")
#     plt.tight_layout()
#     plt.savefig("images/water_log_trends/log_trends_secondary_" + key.lower().replace(" ", "_"))
#     plt.close()
