from countries.Countries import Countries


class HIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Australia', 'Austria', 'Bahrain', 'Belgium', 'Brunei', 'Canada', 'Chile', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Japan', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'New Zealand', 'Norway', 'Oman', 'Poland', 'Portugal', 'Puerto Rico', 'Saudi Arabia', 'Singapore', 'Slovakia', 'Slovenia', 'South Korea', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Trinidad and Tobago', 'United Arab Emirates', 'United Kingdom', 'United States']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = HIC()
    papers = a.all_papers
    print(len(papers))
    print(dict(sorted(a.get_themes_distribution().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution())
    print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution_secondary())
    # i = 0
    # for paper in papers:
    #     if i == 20:
    #         break
    #     i = i + 1
    #     print(paper)


