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

    # Get a list of all the papers and keywords

    def get_all_papers(self):
        sql = 'SELECT * FROM `PAPERS`'
        result = self.db.exec_select(sql).fetchall()
        return result

    def get_all_keywords(self):
        sql = 'SELECT * FROM `PAPER_KEYWORDS`'
        result = self.db.exec_select(sql).fetchall()
        return result

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
        result = self.db.exec_select(sql, (author,)).fetchall()
        return result

    # Getting papers from keywords in various forms

    def get_papers_from_keyword(self, keyword):
        sql = 'SELECT * FROM `PAPER_KEYWORDS` INNER JOIN `PAPERS` ON `PAPER_KEYWORDS`.PAPER_ID=`PAPERS`.ID ' \
              'WHERE KEYWORD=?'
        result = self.db.exec_select(sql, (keyword.lower(),)).fetchall()
        return result

    def get_top_papers_from_keyword(self, keyword):
        paper_keywords = {}
        result_list = self.get_papers_from_keyword(keyword)
        for result_dict in result_list:
            paper_id = result_dict.get('PAPER_ID')
            weight = result_dict.get('WEIGHT')
            if paper_id not in paper_keywords:
                paper_keywords.update({paper_id: weight})
            else:
                old_weight = paper_keywords.get(paper_id)
                paper_keywords.update({paper_id: weight + old_weight})
        return sorted(paper_keywords.items(), key=lambda x: x[1], reverse=True)

    def get_top_10_papers_from_keyword(self, keyword):
        papers = self.get_top_papers_from_keyword(keyword)
        print("Total number of papers mentioning " + keyword + " is " + str(len(papers)))
        to_return = []
        num_papers = 0
        for paper in papers:
            print("Number of mentions for keyword " + keyword + " is " + str(paper[1]))
            returned = self.get_paper_from_paper_id(paper[0])
            print(returned)
            to_return = to_return + returned
            if num_papers == 9:
                break
            num_papers = num_papers + 1
        return to_return

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
        return keyword_papers

    # Getting papers from list of keywords, (AND and OR operations)

    def get_papers_from_list_of_keywords_and(self, list_of_keywords):
        pass

    def get_papers_from_list_of_keywords_or(self, list_of_keywords):
        pass

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
        return sorted_papers

    def get_top_10_papers_from_phrase(self, phrase):
        papers = self.get_papers_from_phrase(phrase)
        print("Total number of papers mentioning " + phrase + " is " + str(len(papers)))
        to_return = []
        num_papers = 0
        papers = sorted(papers, key=lambda x: x[1], reverse=True)
        for paper in papers:
            print("Number of mentions for keyword " + phrase + " is " + str(paper[1]))
            returned = self.get_paper_from_paper_id(paper[0])
            print(returned)
            to_return = to_return + returned
            if num_papers == 9:
                break
            num_papers = num_papers + 1
        return to_return

    # Hidden methods

    def _get_papers_from_keyword(self, keyword):
        sql = 'SELECT * FROM `PAPER_KEYWORDS` WHERE KEYWORD=?'
        result = self.db.exec_select(sql, (keyword.lower(),)).fetchall()
        return result

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
        to_return = arr1
        for item in arr2:
            if item not in to_return:
                to_return.append(item)
        return to_return

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
