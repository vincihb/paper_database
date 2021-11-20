from data.PaperCache import PaperCache
from amr_categories.Water import Water


class Countries:
    def __init__(self):
        self.lst_of_countries = []
        self.w = Water()
        self.pc = PaperCache()
        self.all_papers = self.get_all_papers()

    def get_all_papers(self):
        to_return = []
        for country in self.lst_of_countries:
            to_return = self.pc.get_papers_or_countries(to_return, self.pc.get_papers_from_country(country))
        return to_return

    def get_papers_from_country(self, country):
        return self.pc.get_papers_from_country(country)

    def get_papers_by_year(self, year):
        to_return = []
        for paper in self.all_papers:
            if paper.get("PUBLISHED_YEAR") == year:
                to_return.append(paper)
        return to_return

    def get_themes_distribution(self):
        dict_themes = {'animals': 0, 'water': 0, 'environment': 0, 'food': 0,
                       'consumption': 0, 'ipc': 0, 'plants': 0, 'randd': 0}
        for key in dict_themes.keys():
            dict_themes.update({key: len(self.pc.get_papers_and_themes(self.all_papers,
                                                                       self.pc.get_papers_from_primary_theme(key)))})
        return dict_themes

    def get_themes_distribution_secondary(self):
        dict_themes = {'animals': 0, 'water': 0, 'environment': 0, 'food': 0,
                       'consumption': 0, 'ipc': 0, 'plants': 0, 'randd': 0}
        for key in dict_themes.keys():
            dict_themes.update({key: len(self.pc.get_papers_and_themes(self.all_papers,
                                                                       self.pc.get_papers_from_secondary_theme(key)))})
        return dict_themes

    def get_watercode_distribution(self):
        dict_watercode = {'green': 0, 'blue': 0, 'brown': 0}
        water_papers = self.pc.get_papers_and_themes(self.all_papers, self.pc.get_papers_from_primary_theme('water'))
        for paper in water_papers:
            key = self.w.get_watercode_from_paper(paper)
            dict_watercode.update({key.get('WATER_CODE'): dict_watercode.get(key.get('WATER_CODE')) + 1})
        return dict_watercode

    def get_watercode_distribution_secondary(self):
        dict_watercode = {'green': 0, 'blue': 0, 'brown': 0}
        water_papers = self.pc.get_papers_and_themes(self.all_papers, self.pc.get_papers_from_secondary_theme('water'))
        for paper in water_papers:
            key = self.w.get_watercode_from_paper(paper)
            dict_watercode.update({key.get('WATER_CODE'): dict_watercode.get(key.get('WATER_CODE')) + 1})
        return dict_watercode
