from countries.Countries import Countries


class UMIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = "Albania, Gabon, Namibia, American Samoa, Georgia, " \
                                "North Macedonia, Argentina, Grenada, Panama, Armenia, Guatemala, Paraguay, " \
                                "Azerbaijan, Guyana, Peru, Belarus, Iraq, Romania, Bosnia and Herzegovina, " \
                                "Jamaica, Russian Federation, Russia, Botswana, Jordan, Serbia, Brazil, " \
                                "Kazakhstan, South Africa, Bulgaria, Kosovo, St. Lucia, China, Lebanon, " \
                                "St. Vincent and the Grenadines, Colombia, Libya, " \
                                "Suriname, Costa Rica, Malaysia, Thailand, Cuba, Maldives, Tonga, Dominica, " \
                                "Marshall Islands, Turkey, Dominican Republic, Mauritius, " \
                                "Turkmenistan, Equatorial Guinea, Mexico, Tuvalu, Ecuador, Moldova, Fiji, Montenegro"
        self.lst_of_countries = self.lst_of_countries.split(", ")


if __name__ == "__main__":
    a = UMIC()
    papers = a.get_all_papers()
    print(len(papers))
    i = 0
    for paper in papers:
        if i == 20:
            break
        i = i + 1
        print(paper)