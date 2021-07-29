from data.PaperCache import PaperCache


class Water:
    def __init__(self):
        self.pc = PaperCache()
        self._water_codes = ['green', 'blue', 'wastewater']
        self._subcategories = {}
        self._keywords_to_subcategories = {}
        self._populate_subcategories()

    def _populate_subcategories(self):
        index = 0
        for water_codes in self._water_codes:
            if index == 0:
                list_of_sub = ["Surface Water", "Groundwater", "Karst Groundwater", "Stormwater"]
            elif index == 1:
                list_of_sub = ["Residential Use", "Industrial Use"]
            else:
                list_of_sub = ["Agricultural", "Industrial", "Municipal/Residential", "Pharm. Waste"]
            self._subcategories.update({water_codes: list_of_sub})
            index = index + 1

        index = 0
        for list_of_sub in self._subcategories.values():
            for subcat in list_of_sub:
                if index == 0:
                    keywords = ["river", "lake", "stream"]
                elif index == 1:
                    keywords = ["watertable", "artesian water", "aquifers"]
                elif index == 2:
                    keywords = ["karst", "dissolution type landscape"]
                elif index == 3:
                    keywords = ["runoff", "untreated", "rainfall"]
                elif index == 4:
                    keywords = ["household"]
                elif index == 5:
                    keywords = []
                elif index == 6:
                    keywords = ["irrigation", "crop", "animal waste"]
                elif index == 7:
                    keywords = []
                elif index == 8:
                    keywords = ["sewage"]
                else:
                    keywords = ["laboratory", "pharmaceutical", "drug development"]
                self._keywords_to_subcategories.update({subcat: keywords})
                index = index + 1

    def get_papers_watercode(self, watercode):
        if watercode.lower() not in self._water_codes:
            print(watercode + " is not a water code! Please select watercode from the following:")
            print(self._water_codes)
            return []
        subcategories = self._subcategories.get(watercode.lower())
        to_input = []
        for subcat in subcategories:
            to_input = to_input + self._keywords_to_subcategories.get(subcat)
        return self.pc.get_papers_from_list_of_keywords_or(to_input)


    @property
    def watercodes(self):
        return self._water_codes

    @property
    def keywords_to_subcategories(self):
        return self._keywords_to_subcategories

    @property
    def subcategories(self):
        return self._subcategories


if __name__ == "__main__":
    w = Water()
    print(w.watercodes)
    print(w.subcategories)
    papers = w.get_papers_watercode('Blue')
    print(len(papers))
    # for paper in papers:
    #     print(paper)
