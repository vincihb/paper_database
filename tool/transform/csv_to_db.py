from data.PaperCache import PaperCache
from os import path
import csv
import time
from nltk import word_tokenize
from nltk.corpus import stopwords


def populate_paper_cache():
    print("Populating paper cache")
    local_dir = path.dirname(path.abspath(__file__))
    object_path = path.join(local_dir, '..', '..', 'data', "papers.csv")
    pc = PaperCache()
    with open(object_path) as csv_file:
        data = csv.reader(csv_file)
        index = 0
        for lines in data:
            if index == 0:
                print(lines)
                index = index + 1
                continue
            if pc.get_paper_from_paper_doi(lines[10]):
                continue
            if lines[3] == '':
                published_year = 0
            else:
                published_year = int(lines[3])
            if lines[6] == '' or '-' in lines[6] or ' ' in lines[6] or '/' in lines[6]:
                volume = 0
            else:
                volume = int(lines[6])
            alphabeta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if lines[7] == '' or lines[7][0] in alphabeta or '.' in lines[7] or ' ' in lines[7] or '-' in lines[7] \
                    or 's' in lines[7] or 'e' in lines[7] or '/' in lines[7]:
                issue = 0
            else:
                issue = int(lines[7])
            pc.store_paper(index, lines[10], lines[0], lines[2], published_year, lines[5], volume, issue,
                           lines[8], int(lines[12][1:]))
            index = index + 1
    print("Finished populating paper table")


def extract_keywords(text):
    text = text.lower()
    tokens = word_tokenize(text)
    bag_of_words = [w for w in tokens if w.isalpha()]
    bag_of_key_words = [w for w in bag_of_words if w not in stopwords.words('english')]
    return bag_of_key_words


def populate_keywords():
    print("Adding keywords")
    pc = PaperCache()
    papers = pc.get_all_papers()
    for paper in papers:
        title = paper.get('TITLE')
        abstract = paper.get('ABSTRACT')
        paper_id = paper.get('ID')
        total_bag_of_keywords = extract_keywords(title) + extract_keywords(abstract)
        dictionary_of_keywords = {i: total_bag_of_keywords.count(i) for i in total_bag_of_keywords}
        for keyword in dictionary_of_keywords.keys():
            pc.store_keyword_to_paper(keyword, paper_id, dictionary_of_keywords.get(keyword))
    print("Finished Adding Keywords")


if __name__ == "__main__":
    populate_paper_cache()
    populate_keywords()
    pc = PaperCache()
    look_up = "British Columbia"
    pc.get_top_10_papers_from_phrase(look_up)


