from data.PaperCache import PaperCache
from os import path
import csv
import time


def populate_paper_cache():
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
            if pc.get_paper_from_paper_id(lines[10]):
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
            pc.store_paper(lines[10], lines[0], lines[2], published_year, lines[5], volume, issue,
                           lines[8], int(lines[12][1:]))


if __name__ == "__main__":
    populate_paper_cache()
