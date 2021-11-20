from countries.Countries import Countries


class EastAsia(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Australia', 'Brunei', 'Cambodia', 'China', 'East Timor', 'Indonesia', 'Japan', 'Malaysia', 'Myanmar', 'New Zealand', 'Philippines', 'Singapore', 'South Korea', 'Taiwan', 'Thailand', 'Vanuatu', 'Vietnam']
        # print([val.get('COUNTRY_NAME') for val in self.pc.get_all_countries()])
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = EastAsia()
    papers = a.all_papers
    print(len(papers))
    print(dict(sorted(a.get_themes_distribution().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution())
    print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution_secondary())
