from countries.Countries import Countries


class SouthAsia(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Nepal', 'Pakistan', 'Sri Lanka']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = SouthAsia()
    papers = a.all_papers
    print(len(papers))
    # print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    # print(a.get_watercode_distribution_secondary())
