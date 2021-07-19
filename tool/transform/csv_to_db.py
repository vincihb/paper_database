from data.PaperCache import PaperCache
from os import path
import csv


def populate_paper_cache():
    local_dir = path.dirname(path.abspath(__file__))
    object_path = path.join(local_dir, '..', '..', 'data', "papers.csv")
    with open(object_path) as csv_file:
        data = csv.reader(csv_file)
        for lines in data:
            print(lines)


if __name__ == "__main__":
    populate_paper_cache()
