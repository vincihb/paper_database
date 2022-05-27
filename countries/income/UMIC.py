from countries.Countries import Countries


class UMIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = ['Albania', 'Argentina', 'Azerbaijan', 'Belarus', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'China', 'Colombia', 'Costa Rica', 'Cuba', 'Gabon', 'Georgia', 'Iraq', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kosovo', 'Lebanon', 'Malaysia', 'Mexico', 'Montenegro', 'Peru', 'Romania', 'Russia', 'Serbia', 'South Africa', 'Suriname', 'Thailand', 'Turkey']
        self.all_papers = self.get_all_papers()


if __name__ == "__main__":
    a = UMIC()
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