from data.PaperCache import PaperCache


class Countries:
    def __init__(self):
        self.lst_of_countries = []
        self.pc = PaperCache()

    def get_all_papers(self):
        to_return = []
        for country in self.lst_of_countries:
            to_return = self.pc.get_papers_or_countries(to_return, self.pc.get_papers_from_country(country))
        return to_return

    def get_papers_from_country(self, country):
        return self.pc.get_papers_from_country(country)
