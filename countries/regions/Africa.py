from countries.Countries import Countries


class Africa(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Benin', 'Botswana', 'Burkina Faso', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of Congo', 'Eswatini', 'Ethiopia', 'Gabon', 'Ghana', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Madagascar', 'Malawi', 'Republic of Congo', 'Rwanda', 'South Africa', 'Sudan', 'Tanzania', 'Zambia', 'Zimbabwe']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = Africa()
    papers = a.all_papers
    print(len(papers))
    print(dict(sorted(a.get_themes_distribution().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution())
    print(dict(sorted(a.get_themes_distribution_secondary().items(), key=lambda x: x[1], reverse=True)))
    print(a.get_watercode_distribution_secondary())
