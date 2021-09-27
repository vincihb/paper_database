import json
import os

countries_name = "Eswatini	Ghana	Kenya	Liberia	Nigeria	Sierra Leone	South Africa	Tanzania	Canada	United " \
                 "States	Afghanistan	Iran	Iraq	Jordan	Libya	Pakistan	Finland	Sweden	Tajikistan	" \
                 "India	Maldives	Cambodia	Micronesia	Philippine	Singapore".split("\t")
countries_region = "AFR: LIC	AFR: LIC	AFR: LIC	AFR: LIC	AFR: LIC	AFR: LIC	AFR: MIC	AFR: LIC	AMR: " \
                   "HIC	AMR: HIC	EMR: LIC	EMR: MIC	EMR: MIC	EMR: MIC	EMR: MIC	EMR: LIC	EUR: " \
                   "HIC	EUR: HIC	EUR: LIC	SEAR: LIC	SEAR: MIC	WPR: LIC	WPR: LIC	WPR: LIC	WPR: " \
                   "HIC".split("\t")
countries_environment = "17	13	27	18	14	40	0	33	13	14	16	13	27	0	" \
                        "18	13	10	67	29	25	18	25	0	13	28".split("\t")
countries_clean_water = "15	3	6	15	11	13	9	5	3	5	6	11	16	6	" \
                        "9	11	0	14	13	7	10	6	15	2	15".split("\t")
countries_environmental_contamination = "11	17	6	14	21	15	0	12	3	8	19	12	8	" \
                                        "0	1	5	6	16	11	22	11	14	0	7	10".split("\t")
arr_611 = ["0 41.41 0 0 21.67 10.62 0 0 99.04 97.33 27.59 93.98 59.65 85.7 0 35.84 99.64 99.75 55.24 0 0 27.76 0 "
           "47.46 100".split(" "),
           "70.75 0 61.63 75.26 0 0 93.89 60.72 0 0 0 0 0 0 99.89 0 0 0 0 90.49 99.54 0 88.31 0 0".split(" "),
           "0 44.38 0 0 55.94 53.15 0 0 0.18 2.56 47.5 3.5 38.7 13.24 0 54.31 0.36 0.08 26.62 0 0 43.46 0 46.64 0".split(
               " "),
           "9.51 6.59 9.54 8.7 4.98 9.02 2.77 11.29 0 0 1.45 1.94 0.89 0.15 0 3.82 0 0 2.57 4.98 0.05 13.9 0 2.86 0".split(
               " "),
           "9.84 2.81 9.78 3.49 11.8 15.56 1.41 14.52 0.78 0.12 14.56 0.51 0 0.85 0.11 4.41 0 0.17 3.42 3.96 0.41 "
           "5.68 11.69 3.03 0".split(" "),
           "9.9 4.81 19.05 12.55 5.61 11.65 1.93 13.48 0 0 8.9 0.07 0.75 0.06 0 1.62 0 0 12.16 0.56 0 9.2 7 0 0".split(
               " ")]
arr_611_keys = "Percentage of safely managed drinking water service	" \
               "Percentage of at least basic drinking water service	" \
               "Percentage of basic water service	" \
               "Percentage of limited water service	" \
               "Percentage of unimproved water service	" \
               "Percentage of surface water usage".split("\t")

arr_621 = ["0 13.32 0 0 30.51 14.05 0 26.33 84.37 98.26 0 0 42.88 "
           "82.27 21.62 0 84.1 94.93 0 45.91 0 0 0 60.64 100".split(" "),
           "64.29 0 32.7 18.16 0 0 78.47 0 0 0 50.5 90.27 0 0 0 68.4 0 0 96.77 0 99.16 68.77 88.31 0 0".split(" "),
           "0 10.38 0 0 12.21 2.46 0 5.43 14.66 1.42 0 0 57.09 14.81 70.49 0 15.35 4.36 0 25.36 0 0 0 21.62 0".split(
               " "),
           "21.63 47.44 25.47 29.33 19.54 37.92 14.76 18.66 0 0 10.94 9.73 0 1.66 7.15 10.53 0.55 0.7 2.6 12.1 0.3 "
           "8 0 11.12 0".split(" "),
           "10.26 11.08 33.32 14.82 19.08 29.18 6.54 38.68 0.97 0.32 27.77 0 0.03 1.15 0 13.77 0 0.01 0.63 1.71 "
           "0.55 3.95 11.69 2.84 0".split(" "), "3.81 17.78 8.51 37.68 18.66 16.39 0.22 10.89 0 0 10.78 0.37 0 "
                                                "0.11 0.75 7.3 0 0 0 14.93 0 19.28 9.5 3.79 0".split(" ")]
arr_621_keys = "Percentage of safely managed sanitation service	" \
               "Percentage of at least basic sanitation service	" \
               "Percentage of basic sanitation service	" \
               "Percentage of limited sanitation service	" \
               "Percentage of unimproved sanitation service	" \
               "Percentage of open defecation".split("\t")

arr_631 = ["17.91 12.13 -1 -1 48.29 8.39 61.29 -1 77.06 91.06 "
           "-1 22.07 37.09 82 16.63 -1 92.28 95.2 -1 26.56 -1 -1 -1 43 100".split(" ")]
arr_631_keys = ["Percentage of domestic wastewater safely treated"]

arr_632 = ["87.5 -1 86.5 50 12.5 41.7 52.1 85.3 82.2 33.7 -1 -1"
           " -1 100 -1 -1 96.8 48.4 -1 -1 -1 -1 -1 -1 100".split(" "),
           "87.5 -1 90.4 33.3 15.1 41.7 52.3 87 82.2 32.6 -1 -1"
           " -1 66.7 -1 -1 100 34.6 -1 -1 -1 -1 -1 -1 -1".split(" "),
           "-1 -1 33.3 100 7.8 -1 43.5 80 -1 44.7 -1 -1 -1 100 -1 -1 100 53 -1 -1 -1 -1 -1 -1 100".split(" "),
           "-1 -1 90.3 -1 -1 -1 74.2 -1 -1 -1 -1 -1 -1 100 -1 -1 86.8 97.6 -1 -1 -1 -1 -1 -1 -1".split(" ")]
arr_632_keys = "Overall percentage of water bodies with good ambient water quality, Percentage of rivers with good " \
               "ambient water quality, Percentage of open water bodies with good ambient water quality, Percentage of " \
               "groundwater with good ambient water quality".split(", ")

arr_661 = ["56.17 6064.95 11584.41 197.99 4212.87 155.9 3415.37 55582.32 698030.27 "
           "154786.25 580.46 57712.02 4210.86 446.72 59.64 2468.87 30116.2 "
           "35683.82 1540.07 16686.13 16.72 1875.94 4.16 6102.27 36.98".split(" ")]
arr_661_keys = ['Size of water-related ecosystems in km squared']

country_data = {}
index = 0
while index < len(countries_name):
    country = countries_name[index]
    country_data.update({country: {}})
    data = country_data.get(country)
    data.update({"Region": countries_region[index].split(": ")[0],
                 "Income": countries_region[index].split(": ")[1],
                 "Environment": float(countries_environment[index]),
                 "Clean water and sanitation": float(countries_clean_water[index]),
                 "Environmental contamination": float(countries_environmental_contamination[index]),
                 "6.1.1": dict(zip(arr_611_keys, [float(a[index]) for a in arr_611])),
                 "6.2.1": dict(zip(arr_621_keys, [float(a[index]) for a in arr_621])),
                 "6.3.1": dict(zip(arr_631_keys, [float(a[index]) for a in arr_631])),
                 "6.3.2": dict(zip(arr_632_keys, [float(a[index]) for a in arr_632])),
                 "6.6.1": dict(zip(arr_661_keys, [float(a[index]) for a in arr_661]))})
    index = index + 1

print(country_data)
print(os.getcwd())
if not os.path.exists("data"):
    os.mkdir("data")
if not os.path.exists("data/country_data.json"):
    with open('data/country_data.json', 'w') as file:
        json.dump(country_data, file, indent=4)

