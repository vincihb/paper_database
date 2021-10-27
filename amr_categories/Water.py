from data.PaperCache import PaperCache
from nltk import word_tokenize
from nltk.corpus import stopwords


class Water:
    def __init__(self):
        self.pc = PaperCache()
        self._water_codes = ['green', 'blue', 'brown']
        self._subcategories = {}
        self._keywords_to_subcategories = {}
        self._populate_subcategories()

    def _populate_subcategories(self):
        index = 0
        for water_codes in self._water_codes:
            if index == 0:
                list_of_sub = ["Surface Water", "Marine Water", "Groundwater", "Karst Groundwater"]
            elif index == 1:
                list_of_sub = ["Municipal", "Well", "Self-supplied"]
            else:
                list_of_sub = ["Agricultural", "Industrial", "Municipal", "Pharmaceutical",
                               "Stormwater", "Hospital"]
            self._subcategories.update({water_codes: list_of_sub})
            index = index + 1

        index = 0
        for list_of_sub in self._subcategories.values():
            for subcat in list_of_sub:
                if index == 0:
                    keywords = "surface water, river, lake, stream, tributary, creek".split(", ")
                elif index == 1:
                    keywords = "sea, ocean, saline, estuary, brackish, salt".split(", ")
                elif index == 2:
                    keywords = "aquifer, groundwater, confined aquifer, " \
                               "unconfined aquifer, granular aquifers, alluvial aquifers".split(", ")
                elif index == 3:
                    keywords = "Karst, karst aquifer, karst groundwater, " \
                               "limestone, carbonate, dissolution-type landscape".split(", ")
                elif index == 4:
                    keywords = "household, drinking water, human use, " \
                               "treatment system, distribution system, regulated source".split(", ")
                elif index == 5:
                    keywords = "well water, private well, self-regulated".split(", ")
                elif index == 6:
                    keywords = "glacier melt, fog harvesting, rainwater harvesting, " \
                               "cistern, untreated river water".split(", ")
                elif index == 7:
                    keywords = "irrigation run off, animal waste, " \
                               "manure runoff, feed by-product, pesticides, herbicides, " \
                               "insecticides, nutrient runoff".split(", ")
                elif index == 8:
                    keywords = "industrial waste, heavy metals, high dissolved solids, " \
                               "organic compounds, toxic, energy production".split(", ")
                elif index == 9:
                    keywords = "wastewater, sewage, wastewater treatment plant, household, " \
                               "human waste, primary treatment, secondary treatment, tertiary treatment".split(", ")
                elif index == 10:
                    keywords = "drug development, antibiotic byproduct".split(", ")
                elif index == 11:
                    keywords = "surface runoff, urban runoff, industrial runoff, agriculture runoff, " \
                               "nonpoint source water, precipitation/rainfall, " \
                               "drainage feature, class V injection well".split(", ")
                else:
                    keywords = "clinical waste, clinical antibiotics, clinical viruses".split(", ")
                self._keywords_to_subcategories.update({subcat: keywords})
                index = index + 1

    def get_papers_from_watercode(self, watercode):
        if watercode.lower() not in self._water_codes:
            print(watercode + " is not a water code! Please select watercode from the following:")
            print(self._water_codes)
            return []
        subcategories = self._subcategories.get(watercode.lower())
        to_input = []
        for subcat in subcategories:
            to_input = to_input + self._keywords_to_subcategories.get(subcat)
        to_input = list(dict.fromkeys(to_input))
        return self.pc.get_papers_and_themes(self.pc.get_papers_from_list_of_keywords_or(to_input),
                                             self.pc.get_papers_from_primary_theme('water'))

    def get_watercode_from_paper(self, paper):
        dict_to_return = self.get_subcategory_from_paper(paper)
        subcat = dict_to_return.get("SUBCATEGORY")
        for key in self._subcategories:
            if subcat in self._subcategories.get(key):
                dict_to_return.update({'WATER_CODE': key})
                break
        return dict_to_return

    def get_watercode_from_paper_id(self, paper_id):
        dict_to_return = self.get_subcategory_from_paper_id(paper_id)
        subcat = dict_to_return.get("SUBCATEGORY")
        for key in self._subcategories:
            if subcat in self._subcategories.get(key):
                dict_to_return.update({'WATER_CODE': key})
                break
        return dict_to_return

    def get_watercode_from_paper_doi(self, doi):
        dict_to_return = self.get_subcategory_from_paper_doi(doi)
        subcat = dict_to_return.get("SUBCATEGORY")
        for key in self._subcategories:
            if subcat in self._subcategories.get(key):
                dict_to_return.update({'WATER_CODE': key})
                break
        return dict_to_return

    def get_subcategory_from_paper(self, paper):
        keywords = self.pc.get_keywords_from_paper(paper)
        dict_of_subcat = {key: 0 for key in self._keywords_to_subcategories.keys()}
        for keyword in keywords:
            k = keyword.get('KEYWORD')
            for key in self._keywords_to_subcategories.keys():
                if k in self._keywords_to_subcategories.get(key):
                    dict_of_subcat.update({key: keyword.get('WEIGHT') + dict_of_subcat.get(key)})
        subcat = ""
        max_val = 0
        for key in dict_of_subcat.keys():
            val = dict_of_subcat.get(key)
            if val > max_val:
                subcat = key
                max_val = val
        return {'PAPER_ID': keywords[0].get('PAPER_ID'), 'DOI': paper.get('DOI'), 'SUBCATEGORY': subcat}

    def get_subcategory_from_paper_id(self, paper_id):
        keywords = self.pc.get_keywords_from_paper_id(paper_id)
        dict_of_subcat = {key: 0 for key in self._keywords_to_subcategories.keys()}
        for keyword in keywords:
            k = keyword.get('KEYWORD')
            for key in self._keywords_to_subcategories.keys():
                if k in self._keywords_to_subcategories.get(key):
                    dict_of_subcat.update({key: keyword.get('WEIGHT') + dict_of_subcat.get(key)})
        subcat = ""
        max_val = 0
        for key in dict_of_subcat.keys():
            val = dict_of_subcat.get(key)
            if val > max_val:
                subcat = key
                max_val = val
        return {'PAPER_ID': keywords[0].get('PAPER_ID'), 'DOI': self.pc.get_paper_from_paper_id(paper_id)[0].get('DOI'),
                'SUBCATEGORY': subcat}

    def get_subcategory_from_paper_doi(self, doi):
        keywords = self.pc.get_keywords_from_paper_doi(doi)
        dict_of_subcat = {key: 0 for key in self._keywords_to_subcategories.keys()}
        for keyword in keywords:
            k = keyword.get('KEYWORD')
            for key in self._keywords_to_subcategories.keys():
                if k in self._keywords_to_subcategories.get(key):
                    dict_of_subcat.update({key: keyword.get('WEIGHT') + dict_of_subcat.get(key)})
        subcat = ""
        max_val = 0
        for key in dict_of_subcat.keys():
            val = dict_of_subcat.get(key)
            if val > max_val:
                subcat = key
                max_val = val
        return {'PAPER_ID': keywords[0].get('PAPER_ID'), 'DOI': doi, 'SUBCATEGORY': subcat}

    @property
    def watercodes(self):
        return self._water_codes

    @property
    def keywords_to_subcategories(self):
        return self._keywords_to_subcategories

    @property
    def subcategories(self):
        return self._subcategories

    @staticmethod
    def _extract_keywords(text):
        text = text.lower()
        tokens = word_tokenize(text)
        bag_of_words = [w for w in tokens if w.isalpha()]
        bag_of_key_words = [w for w in bag_of_words if w not in stopwords.words('english')]
        return bag_of_key_words


if __name__ == "__main__":
    w = Water()
    print(w.watercodes)
    print(w.subcategories)
    print(w.keywords_to_subcategories)
    papers = w.get_papers_from_watercode('green')
    print(len(papers))
    papers = w.get_papers_from_watercode('blue')
    print(len(papers))
    papers = w.get_papers_from_watercode('brown')
    print(len(papers))
    # index = 0
    # for paper in papers:
    #     print(paper)
    #     if index == 10:
    #         break
    #     index = index + 1
    # print(w.get_watercode_from_paper_id('7195'))
