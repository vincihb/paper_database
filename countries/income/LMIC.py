from countries.Countries import Countries


class LMIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Algeria', 'Bangladesh', 'Benin', 'Bhutan', 'Bolivia', 'Cambodia', 'Cameroon', 'Cape Verde', 'Comoros', 'East Timor', 'Egypt', 'Eswatini', 'Ghana', 'India', 'Indonesia', 'Iran', 'Ivory Coast', 'Kenya', 'Kyrgyzstan', 'Lesotho', 'Morocco', 'Myanmar', 'Nepal', 'Pakistan', 'Palestine', 'Philippines', 'Republic of Congo', 'Sri Lanka', 'Tanzania', 'Tunisia', 'Ukraine', 'Vanuatu', 'Vietnam', 'Zambia', 'Zimbabwe']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = LMIC()
    papers = a.all_papers
    print(len(papers))
    # print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    # print(a.get_watercode_distribution_secondary())
    # papers = a.get_papers_from_country("India")
    # print(len(papers))
    # for paper in papers:
    #     print(paper)


