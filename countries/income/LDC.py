from countries.Countries import Countries


class LDC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Afghanistan', 'Burkina Faso', 'Central African Republic', 'Chad', 'Democratic Republic of Congo', 'Ethiopia', 'Guinea-Bissau', 'Madagascar', 'Malawi', 'Rwanda', 'Sudan']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = LDC()
    papers = a.all_papers
    print(len(papers))
    print(dict(sorted(a.get_themes_distribution().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution())
    print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution_secondary())


