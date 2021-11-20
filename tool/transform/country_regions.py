from data.PaperCache import PaperCache
from os import path
import csv

local_dir = path.dirname(path.abspath(__file__))
object_path = path.join(local_dir, '..', '..', 'data', "CLASS.csv")
pc = PaperCache()
all_countries = [val.get('COUNTRY_NAME') for val in pc.get_all_countries()]
regions = {'East Asia & Pacific': [], 'Europe & Central Asia': [], 'Latin America & Caribbean': [],
           'Middle East & North Africa': [], 'North America': [], 'South Asia': [], 'Sub-Saharan Africa': []}
incomes = {'High income': [], 'Upper middle income': [], 'Lower middle income': [], 'Low income': []}
print(all_countries)
print(len(all_countries))
items = []
with open(object_path) as csv_file:
    data = csv.reader(csv_file)
    for lines in data:
        items.append(lines)

for country in all_countries:
    in_database = False
    for lines in items:
        if lines[0] == country:
            in_database = True
            regions.get(lines[2]).append(country)
            incomes.get(lines[3]).append(country)
            # try:
            #     regions.get(lines[2]).append(country)
            # except:
            #     regions.update({lines[2]: [country]})
            # try:
            #     incomes.get(lines[3]).append(country)
            # except:
            #     incomes.update({lines[3]: [country]})
    if not in_database:
        print("Not in database")
        print(country)

print(regions)
total = 0
for val in regions.values():
    total += len(val)
print(total)
print(incomes)
total = 0
for val in incomes.values():
    total += len(val)
print(total)