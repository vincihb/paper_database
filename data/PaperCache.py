from db.SqlExecutor import SqlExecutor


class PaperCache:
    def __init__(self):
        self.db = SqlExecutor()

    def store_paper(self, paper_id, title, abstract, year, journal, volume, issue, pages, covidence):
        sql = 'INSERT INTO `PAPERS` (ID, TITLE, ABSTRACT, PUBLISHED_YEAR, JOURNAL, VOLUME, ISSUE, PAGES, ' \
              'COVIDENCE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.db.exec_insert(sql, (paper_id, title, abstract, year, journal, volume, issue, pages, covidence))

    def store_keyword_to_paper(self, keyword, paper_id, weight):
        sql = 'INSERT INTO `PAPER_KEYWORDS` (KEYWORD, PAPER_ID, WEIGHT) VALUES (?, ?, ?)'
        self.db.exec_insert(sql, (keyword, paper_id, weight))

    def get_all_papers(self):
        sql = 'SELECT * FROM `PAPERS`'
        result = self.db.exec_select(sql).fetchall()
        return result

    def get_paper_from_paper_id(self, paper_id):
        sql = 'SELECT * FROM `PAPERS` WHERE ID=?'
        result = self.db.exec_select(sql, (paper_id,)).fetchall()
        return result

    def get_paper_from_year(self, year):
        sql = 'SELECT * FROM `PAPERS` WHERE PUBLISHED_YEAR=?'
        result = self.db.exec_select(sql, (year,)).fetchall()
        return result

    def get_papers_from_author(self, author):
        sql = 'SELECT * FROM `AUTHORS` INNER JOIN `PAPER` ON `AUTHORS`.PAPER_ID=`PAPER`.ID WHERE AUTHOR=?'
        result = self.db.exec_select(sql, (author,)).fetchall()
        return result

    def get_papers_from_keyword(self, keyword):
        sql = 'SELECT * FROM `PAPER_KEYWORDS` WHERE KEYWORD=?'
        result = self.db.exec_select(sql, (keyword,)).fetchall()
        return result

    def get_top_papers_from_keywords(self, keywords):
        bill_keyword = {}
        for keyword in keywords:
            result_list = self.get_papers_from_keyword(keyword)
            for result_dict in result_list:
                bill_id = result_dict.get('PAPER_ID')
                weight = result_dict.get('WEIGHT')
                if bill_id not in bill_keyword:
                    bill_keyword.update({bill_id: weight})
                else:
                    old_weight = bill_keyword.get(bill_id)
                    bill_keyword.update({bill_id: weight + old_weight})
        return sorted(bill_keyword.items(), key=lambda x: x[1], reverse=True)

    def get_all_keywords(self):
        sql = 'SELECT * FROM `PAPER_KEYWORDS`'
        result = self.db.exec_select(sql).fetchall()
        return result
