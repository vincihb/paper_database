from countries.Countries import Countries


class Europe(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Albania', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan', 'Kosovo', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Luxembourg', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom']
        # print([val.get('COUNTRY_NAME') for val in self.pc.get_all_countries()])
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = Europe()
    papers = a.all_papers
    print(len(papers))
    # print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    # print(a.get_watercode_distribution_secondary())
