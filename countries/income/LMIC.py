from countries.Countries import Countries


class LMIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = "Angola, Honduras, Philippines, Algeria, India, Samoa, Bangladesh, " \
                                "Indonesia, Sao Tome and Principe, Belize, Iran, Islamic Republic of Iran," \
                                "Senegal, Benin, Kenya, Solomon Islands, Bhutan, Kiribati, Sri Lanka, " \
                                "Bolivia, Kyrgyz Republic, Tanzania, Cabo Verde, Lao PDR, Laos, " \
                                "Lao People's Democratic Republic, Tajikistan, " \
                                "Cambodia, Lesotho, Timor-Leste, Cameroon, Mauritania, Tunisia, Comoros, " \
                                "Micronesia, Ukraine, Republic of Congo, Mongolia, Uzbekistan, " \
                                "Cote d'Ivoire, Ivory Coast, Morocco, Vanuatu, Djibouti, Myanmar, Vietnam, " \
                                "Egypt, Nepal, West Bank and Gaza, El Salvador, Nicaragua, Zambia, " \
                                "Eswatini, Nigeria, Zimbabwe, Ghana, Pakistan, Haiti, Papua New Guinea"
        self.lst_of_countries = self.lst_of_countries.split(", ")


if __name__ == "__main__":
    a = LMIC()
    papers = a.get_all_papers()
    print(len(papers))
    i = 0
    for paper in papers:
        if i == 20:
            break
        i = i + 1
        print(paper)
    # papers = a.get_papers_from_country("India")
    # print(len(papers))
    # for paper in papers:
    #     print(paper)


