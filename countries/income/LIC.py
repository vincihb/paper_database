from countries.Countries import Countries


class LIC(Countries):
    def __init__(self):
        super().__init__()
        self.lst_of_countries = "Democratic People's Republic of Korea, Zimbabwe"
        self.lst_of_countries = self.lst_of_countries.split(", ")


if __name__ == "__main__":
    a = LIC()
    papers = a.get_all_papers()
    print(len(papers))
    i = 0
    for paper in papers:
        if i == 200:
            break
        i = i + 1
        print(paper)


