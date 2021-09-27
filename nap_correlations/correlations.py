import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import json
import os

f = open('data/country_data.json')
country_dict = json.load(f)
y_themes = ["Environment", "Clean water and sanitation", "Environmental contamination"]
x_themes = ["6.1.1", "6.2.1", "6.3.1", "6.3.2", "6.6.1"]
x_themes_subdivisions = {x_theme: [key for key in country_dict.get("Eswatini").get(x_theme).keys()] for x_theme in
                         x_themes}
for y_theme in y_themes:
    print("======")
    print(y_theme)
    for x_theme in x_themes:
        print(x_theme)
        for subdiv in x_themes_subdivisions.get(x_theme):
            x = []
            y = []
            for key in country_dict.keys():
                data = country_dict.get(key)
                if data.get(x_theme).get(subdiv) == -1:
                    continue
                y.append(data.get(y_theme))
                x.append(data.get(x_theme).get(subdiv))
            print("===")
            print(subdiv)
            cov = 1 / (len(x) - 1) * np.sum([(x[i] - np.mean(x)) * (y[i] - np.mean(y)) for i in range(0, len(x))])
            cor = np.sum([(x[i] - np.mean(x)) * (y[i] - np.mean(y)) for i in range(0, len(x))]) \
                  / (np.sqrt(np.sum([(x[i] - np.mean(x)) ** 2 for i in range(0, len(x))]))
                     * np.sqrt(np.sum([(y[i] - np.mean(y)) ** 2 for i in range(0, len(x))])))
            print(cor)
            b = np.mean(y) - cov / np.var(x) * np.mean(x)
            m = cov / np.var(x)
            num_points = 1000
            x_array = [a * ((int(max(x) + 1) - int(min(x) - 5)) / num_points) + int(min(x) - 5) for a in
                       range(0, num_points, 1)]
            y_hat = [m * x_val + b for x_val in x_array]
            r = 1 - np.sum([np.power(m * x[index] + b - y[index], 2) for index in range(0, len(x))]) \
                / np.sum([(y[i] - np.mean(y)) ** 2 for i in range(0, len(x))])
            plt.plot(x_array, y_hat, label="R squared " + str(round(r, 5)))
            plt.xlim(min(x) - 5, max(x) + 1)
            plt.ylim(min(y) - 5, max(y) + 20)
            first_legend = plt.legend(title="Line of best fit", loc="upper right")
            plt.gca().add_artist(first_legend)
            # print(r)
            region_colours = {"afr": "blue", "amr": "cyan", "emr": "green", "eur": "orange", "sear": "red",
                              "wpr": "purple"}
            income_shapes = {"hic": "o", "mic": "^", "lic": "s"}
            for key in country_dict.keys():
                if country_dict.get(key).get(x_theme).get(subdiv) == -1:
                    continue
                plt.plot([country_dict.get(key).get(x_theme).get(subdiv)], [country_dict.get(key).get(y_theme)],
                         color=region_colours.get(country_dict.get(key).get('Region').lower()),
                         marker=income_shapes.get(country_dict.get(key).get('Income').lower()))
            plt.xlabel(subdiv)
            plt.ylabel(y_theme)
            patches = [mpatches.Patch(color=region_colours.get(key),
                                      label=key.upper()) for key in region_colours.keys()]
            second_legend = plt.legend(title="Regions", handles=patches, loc="upper left")
            plt.gca().add_artist(second_legend)
            shapes = [mlines.Line2D([0], [0], color='w',
                                    marker=income_shapes.get(key),
                                    markerfacecolor='black',
                                    label=key.upper(),
                                    markersize=12) for key in income_shapes.keys()]
            plt.legend(title="Income level", handles=shapes, loc=9)
            if not os.path.exists("images"):
                os.mkdir("images")
            if not os.path.exists("images/" + x_theme):
                os.mkdir("images/" + x_theme)
            plt.tight_layout()
            plt.savefig(
                'images/' + x_theme + "/" + subdiv.lower().replace(" ", "_") + "_" + y_theme.lower().replace(" ", "_"))
            plt.close()
