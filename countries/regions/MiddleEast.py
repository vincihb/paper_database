from countries.Countries import Countries


class MiddleEast(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Algeria', 'Bahrain', 'Egypt', 'Iran', 'Iraq', 'Israel', 'Jordan', 'Lebanon', 'Morocco', 'Oman', 'Palestine', 'Saudi Arabia', 'Tunisia', 'United Arab Emirates']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = MiddleEast()
    papers = a.all_papers
    print(len(papers))
    # print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    # print(a.get_watercode_distribution_secondary())
