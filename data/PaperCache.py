from db.SqlExecutor import SqlExecutor
from nltk import word_tokenize
from nltk.corpus import stopwords


class PaperCache:
    def __init__(self):
        self.db = SqlExecutor()

    def store_paper(self, paper_id, doi, title, abstract, year, journal, volume, issue, pages, covidence):
        sql = 'INSERT INTO `PAPERS` (ID, DOI, TITLE, ABSTRACT, PUBLISHED_YEAR, JOURNAL, VOLUME, ISSUE, PAGES, ' \
              'COVIDENCE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.db.exec_insert(sql, (paper_id, doi, title, abstract, year, journal, volume, issue, pages, covidence))

    def store_keyword_to_paper(self, keyword, paper_id, weight):
        sql = 'INSERT INTO `PAPER_KEYWORDS` (KEYWORD, PAPER_ID, WEIGHT) VALUES (?, ?, ?)'
        self.db.exec_insert(sql, (keyword, paper_id, weight))

    def store_author(self, paper_id, author):
        sql = 'INSERT INTO `AUTHORS` (AUTHOR, PAPER_ID) VALUES (?, ?)'
        self.db.exec_insert(sql, (author, paper_id))

    # Fixing the DOI

    def update_doi(self, paper_id, doi):
        sql = 'UPDATE `PAPERS` SET DOI=? WHERE ID=?'
        self.db.exec_update(sql, (doi, paper_id))

    # Get a list of all the papers and keywords 

    def get_all_papers(self):
        sql = 'SELECT * FROM `PAPERS`'
        result = self.db.exec_select(sql).fetchall()
        return result

    def get_all_keywords(self):
        sql = 'SELECT * FROM `PAPER_KEYWORDS`'
        result = self.db.exec_select(sql).fetchall()
        return result

    # Get all keywords from paper

    def get_keywords_from_paper(self, paper):
        paper_id = paper[0].get('ID')
        sql = 'SELECT * FROM `PAPER_KEYWORDS` WHERE PAPER_ID=?'
        result = self.db.exec_select(sql, (paper_id,)).fetchall()
        return sorted(result, key=lambda x: x.get("WEIGHT"), reverse=True)

    def get_keywords_from_paper_id(self, paper_id):
        sql = 'SELECT * FROM `PAPER_KEYWORDS` WHERE PAPER_ID=?'
        result = self.db.exec_select(sql, (paper_id,)).fetchall()
        return sorted(result, key=lambda x: x.get("WEIGHT"), reverse=True)

    def get_keywords_from_paper_doi(self, doi):
        paper = self.get_paper_from_paper_doi(doi)
        paper_id = paper[0].get('ID')
        sql = 'SELECT * FROM `PAPER_KEYWORDS` WHERE PAPER_ID=?'
        result = self.db.exec_select(sql, (paper_id,)).fetchall()
        return sorted(result, key=lambda x: x.get("WEIGHT"), reverse=True)

    # Easy way of searching papers

    def get_paper_from_paper_id(self, paper_id):
        sql = 'SELECT * FROM `PAPERS` WHERE ID=?'
        result = self.db.exec_select(sql, (paper_id,)).fetchall()
        return result

    def get_paper_from_paper_doi(self, doi):
        sql = 'SELECT * FROM `PAPERS` WHERE DOI=?'
        result = self.db.exec_select(sql, (doi,)).fetchall()
        return result

    def get_paper_from_year(self, year):
        sql = 'SELECT * FROM `PAPERS` WHERE PUBLISHED_YEAR=?'
        result = self.db.exec_select(sql, (year,)).fetchall()
        return result

    def get_papers_from_author(self, author):
        sql = 'SELECT * FROM `AUTHORS` INNER JOIN `PAPERS` ON `AUTHORS`.PAPER_ID=`PAPERs`.ID WHERE AUTHOR=?'
        result = self.db.exec_select(sql, (author, )).fetchall()
        return result

    # Getting papers from keywords in various forms

    def get_papers_from_keyword(self, keyword):
        space = " "
        if space in keyword:
            return self.get_papers_from_phrase(keyword)
        sql = 'SELECT * FROM `PAPER_KEYWORDS` INNER JOIN `PAPERS` ON `PAPER_KEYWORDS`.PAPER_ID=`PAPERS`.ID ' \
              'WHERE KEYWORD=?'
        result = self.db.exec_select(sql, (keyword.lower(),)).fetchall()
        return sorted(result, key=lambda x: x.get("WEIGHT"), reverse=True)

    def get_papers_from_keyword_filtered(self, keyword, filters):
        keyword_papers = self.get_papers_from_keyword(keyword)
        index = 0
        while index < len(filters):
            excluding_papers = self.get_papers_from_phrase(filters[index])
            excluding_papers = [item[0] for item in excluding_papers]
            to_return = []
            for paper in keyword_papers:
                if paper.get('PAPER_ID') not in excluding_papers:
                    to_return.append(paper)
            keyword_papers = to_return
            index = index + 1
        return sorted(keyword_papers, key= lambda x: x.get("WEIGHT"), reverse=True)

    # Getting papers from phrases

    def get_papers_from_phrase(self, phrase):
        total_bag_of_keywords = self._extract_keywords(phrase)
        keyword = total_bag_of_keywords[0]
        returned_papers = self._get_papers_from_keyword(keyword)
        sorted_papers = self._sort_papers_by_keyword_weight(returned_papers)
        index = 1
        while index < len(total_bag_of_keywords):
            keyword = total_bag_of_keywords[index]
            new_returned_papers = self.get_papers_from_keyword(keyword)
            new_sorted_papers = self._sort_papers_by_keyword_weight(new_returned_papers)
            sorted_papers = self._intersection_of_papers(sorted_papers, new_sorted_papers)
            index = index + 1
        to_return = []
        for paper_tuple in sorted_papers:
            new_dict = self.get_paper_from_paper_id(paper_tuple[0])[0]
            temp = {'KEYWORD': phrase.lower(), 'PAPER_ID': paper_tuple[0], 'WEIGHT': paper_tuple[1]}
            temp.update(new_dict)
            to_return.append(temp)
        return sorted(to_return, key=lambda x: x.get('WEIGHT'), reverse=True)

    def get_papers_from_phrase_filtered(self, phrase, filters):
        keyword_papers = self._get_papers_from_phrase(phrase)
        index = 0
        while index < len(filters):
            excluding_papers = self._get_papers_from_phrase(filters[index])
            excluding_papers = [item[0] for item in excluding_papers]
            to_return = []
            for paper in keyword_papers:
                if paper[0] not in excluding_papers:
                    to_return.append(paper)
            keyword_papers = to_return
            index = index + 1
        to_return = []
        for paper_tuple in keyword_papers:
            new_dict = self.get_paper_from_paper_id(paper_tuple[0])[0]
            temp = {'KEYWORD': phrase.lower(), 'PAPER_ID': paper_tuple[0], 'WEIGHT': paper_tuple[1]}
            temp.update(new_dict)
            to_return.append(temp)
        return to_return

    # Getting papers from list of keywords, (AND, which is intersection of sets, and OR, which is union of sets,
    # operations)

    def get_papers_from_list_of_keywords_and(self, list_of_keywords):
        phrase = ""
        space = " "
        for word in list_of_keywords:
            phrase = phrase + word + space
        return self.get_papers_from_phrase(phrase)

    def get_papers_from_list_of_keywords_or(self, list_of_keywords):
        paper_keywords = self.get_papers_from_keyword(list_of_keywords[0])
        index = 1
        while index < len(list_of_keywords):
            new_papers = self.get_papers_from_keyword(list_of_keywords[index])
            for result_dict in new_papers:
                paper_id = result_dict.get('PAPER_ID')
                weight = result_dict.get('WEIGHT')
                in_paper_keywords = False
                for paper in paper_keywords:
                    if paper.get('PAPER_ID') == paper_id:
                        old_weight = paper.get('WEIGHT')
                        paper.update({paper_id: weight + old_weight})
                        old_keyword = paper.get('KEYWORD')
                        if list_of_keywords[index] != old_keyword:
                            paper.update({'KEYWORD': old_keyword + ' ' + list_of_keywords[index].lower()})
                        in_paper_keywords = True
                        break
                if not in_paper_keywords:
                    paper_keywords.append(result_dict)
            index = index + 1
        return sorted(paper_keywords, key=lambda x: x.get('WEIGHT'), reverse=True)

    # Hidden methods

    def _get_papers_from_keyword(self, keyword):
        sql = 'SELECT * FROM `PAPER_KEYWORDS` WHERE KEYWORD=?'
        result = self.db.exec_select(sql, (keyword.lower(),)).fetchall()
        return result

    def _get_papers_from_phrase(self, phrase):
        total_bag_of_keywords = self._extract_keywords(phrase)
        keyword = total_bag_of_keywords[0]
        returned_papers = self._get_papers_from_keyword(keyword)
        sorted_papers = self._sort_papers_by_keyword_weight(returned_papers)
        index = 1
        while index < len(total_bag_of_keywords):
            keyword = total_bag_of_keywords[index]
            new_returned_papers = self.get_papers_from_keyword(keyword)
            new_sorted_papers = self._sort_papers_by_keyword_weight(new_returned_papers)
            sorted_papers = self._intersection_of_papers(sorted_papers, new_sorted_papers)
            index = index + 1
        return sorted_papers

    @staticmethod
    def _sort_papers_by_keyword_weight(result_list):
        paper_keywords = {}
        for result_dict in result_list:
            paper_id = result_dict.get('PAPER_ID')
            weight = result_dict.get('WEIGHT')
            if paper_id not in paper_keywords:
                paper_keywords.update({paper_id: weight})
            else:
                old_weight = paper_keywords.get(paper_id)
                paper_keywords.update({paper_id: weight + old_weight})
        return sorted(paper_keywords.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def _union_of_papers(arr1, arr2):
        for item in arr2:
            if item not in arr1:
                arr1.append(item)
        return arr1

    @staticmethod
    def _intersection_of_papers(arr1, arr2):
        to_return = []
        for item in arr1:
            to_return = to_return + [thing for thing in arr2 if item[0] in thing]
        return to_return

    @staticmethod
    def _extract_keywords(text):
        text = text.lower()
        tokens = word_tokenize(text)
        bag_of_words = [w for w in tokens if w.isalpha()]
        bag_of_key_words = [w for w in bag_of_words if w not in stopwords.words('english')]
        return bag_of_key_words
