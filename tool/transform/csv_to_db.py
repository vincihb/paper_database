from sqlite3 import IntegrityError
import time
import random
from data.PaperCache import PaperCache
from os import path
import csv
from nltk import word_tokenize
from nltk.corpus import stopwords
from flashgeotext.geotext import GeoText
from multiprocessing import Process
from amr_categories import *


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
                index = index + 1
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


def populate_author_cache():
    print("Populating author cache")
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
            authors = lines[1].split(';')
            paper_id = pc.get_paper_from_paper_doi(lines[10])[0].get('ID')
            for author in authors:
                if ',' not in author:
                    continue
                name = author.split(',')
                if name[0][0] == ' ':
                    author_name = name[1][1:] + name[0]
                else:
                    author_name = name[1][1:] + ' ' + name[0]
                papers = pc.get_papers_from_author(author_name)
                store_paper = True
                for paper in papers:
                    if paper.get('ID') == paper_id:
                        store_paper = False
                if store_paper:
                    pc.store_author(paper_id, author_name)
            index = index + 1
    print("Finished populating author table")


def populate_sector():
    print("Populating paper cache")
    local_dir = path.dirname(path.abspath(__file__))
    object_path = path.join(local_dir, '..', '..', 'data', "papers.csv")
    pc = PaperCache()
    with open(object_path) as csv_file:
        data = csv.reader(csv_file)
        index = 0
        http_string = "http://dx.doi.org/"
        https_string = "https://dx.doi.org/"
        for lines in data:
            if index == 0:
                print(lines[-6])
                index = index + 1
                continue
            doi = lines[-6]
            if http_string in doi:
                doi = doi[len(http_string):]
            elif https_string in doi:
                doi = doi[len(https_string):]
            try:
                sector = lines[-1].split(" - ")[1]
            except:
                sector = "Not defined"
            try:
                pc.store_sector(sector, pc.get_paper_from_paper_doi(doi)[0].get('ID'))
            except:
                print("Unique constraint!")
            index = index + 1


def parallelization(lines, geotext, pc):
    http_string = "http://dx.doi.org/"
    https_string = "https://dx.doi.org/"
    doi = lines[-6]
    if http_string in doi:
        doi = doi[len(http_string):]
    elif https_string in doi:
        doi = doi[len(https_string):]
    title_abstract = lines[0] + ' ' + lines[2]
    countries = geotext.extract(title_abstract).get('countries')
    countries = list(dict.fromkeys(countries))
    for country in countries:
        try:
            pc.store_country(country, pc.get_paper_from_paper_doi(doi)[0].get('ID'))
        except IntegrityError:
            print(lines)
            print("DOI: " + str(doi) + ", country: " + str(country))


def populate_country():
    print("Populating paper cache")
    local_dir = path.dirname(path.abspath(__file__))
    object_path = path.join(local_dir, '..', '..', 'data', "papers.csv")
    pc = PaperCache()
    geotext = GeoText()
    with open(object_path) as csv_file:
        data = csv.reader(csv_file)
        index = 0
        processes = []
        for lines in data:
            if lines[-6] == "":
                continue
            if index == 0:
                print(lines[0] + ' ' + lines[2])
                index = index + 1
                continue
            p = Process(target=parallelization, args=(lines, geotext, pc))
            p.start()
            processes.append(p)
            index = index + 1
            if index % 10 == 0:
                for process in processes:
                    process.join()
                processes = []
                # time.sleep(1)


def fix_doi():
    pc = PaperCache()
    papers = pc.get_all_papers()
    http_string = "http://dx.doi.org/"
    https_string = "https://dx.doi.org/"
    for paper in papers:
        doi = paper.get('DOI')
        if http_string in doi:
            print(paper)
            pc.update_doi(paper.get('ID'), doi[len(http_string):])
        elif https_string in doi:
            print(paper)
            pc.update_doi(paper.get('ID'), doi[len(https_string):])


def get_theme(pc, paper_id):
    themes_class_dict = {'ipc': HumanIPC.HumanIPC(), 'consumption': HumanConsumption.HumanConsumption(),
              'water': CleanWater.CleanWater(), 'environment': Environment.Environment(),
              'food': FoodSafety.FoodSafety(), 'animals': Animals.Animals(), 'plants': Plants.Plants(),
              'randd': RAndD.RAndD()}
    theme_dict = {'ipc': 0, 'consumption': 0, 'water': 0, 'environment': 0, 'food': 0, 'animals': 0,
                  'plants': 0, 'randd': 0}
    for key in themes_class_dict.keys():
        theme_dict.update({key: themes_class_dict.get(key).get_weighting_theme_from_paper_id(paper_id)})
    print(theme_dict)
    sorted_themes = list(dict(sorted(theme_dict.items(), key=lambda x: x[1], reverse=True)).keys())
    print(sorted_themes)


def populate_parallel(pc, paper_id, themes_class_dict):
    theme_dict = {'ipc': 0, 'consumption': 0, 'water': 0, 'environment': 0, 'food': 0, 'animals': 0,
                  'plants': 0, 'randd': 0}
    for key in themes_class_dict.keys():
        theme_dict.update({key: themes_class_dict.get(key).get_weighting_theme_from_paper_id(paper_id)})
    sorted_themes = list(dict(sorted(theme_dict.items(), key=lambda x: x[1], reverse=True)).keys())
    if int(paper_id) % 100 == 0:
        print(paper_id)
    primary_theme = sorted_themes[0]
    if theme_dict.get(sorted_themes[1]) == theme_dict.get(sorted_themes[2]):
        secondary_theme = 'None'
    else:
        secondary_theme = sorted_themes[1]
    # print(theme_dict)
    # print(sorted_themes)
    try:
        pc.store_theme(primary_theme, secondary_theme, paper_id)
    except IntegrityError:
        print("nm")
        print(paper_id)
        print(primary_theme)
        print(secondary_theme)


def populate_theme():
    pc = PaperCache()
    all_papers = pc.get_all_papers()
    themes = {'ipc': HumanIPC.HumanIPC(), 'consumption': HumanConsumption.HumanConsumption(),
              'water': CleanWater.CleanWater(), 'environment': Environment.Environment(),
              'food': FoodSafety.FoodSafety(), 'animals': Animals.Animals(), 'plants': Plants.Plants(),
              'randd': RAndD.RAndD()}
    processes = []
    index = 0
    process_num = 45
    prev_time = [1000000]
    start_time = time.time()
    for paper in all_papers:
        # print(paper.get('ID'))
        # print(paper.get('TITLE'))
        # print(paper.get("ABSTRACT"))
        # populate_parallel(pc, paper.get('ID'), themes)
        if pc.get_paper_theme(paper.get('ID')):
            continue
        p = Process(target=populate_parallel, args=(pc, paper.get('ID'), themes))
        p.start()
        processes.append(p)
        index = index + 1
        if index % process_num == 0:
            index = 0
            for process in processes:
                process.join()
            elapsed_time = time.time() - start_time
            if float(elapsed_time)/float(process_num) <= min(prev_time) or random.randrange(0, 2) == 1:
                process_num += 1
            else:
                process_num -= 1
            prev_time = [min(prev_time), float(elapsed_time) / float(process_num)]
            start_time = time.time()
            print(process_num)
            processes = []


if __name__ == "__main__":
    # populate_paper_cache()
    # populate_keywords()
    # populate_author_cache()
    # fix_doi()
    # populate_sector()
    # populate_country()
    # get_theme(PaperCache(), '530')
    # populate_theme()
    # print("Done")
    pc = PaperCache()
    # get_theme(pc, '700')
    # print(pc.get_paper_from_paper_id('700'))

    themes = {'ipc': 0, 'consumption': 0, 'water': 0, 'environment': 0, 'food': 0,
              'animals': 0, 'plants': 0, 'randd': 0}
    themes = list(themes.keys())
    for theme in themes:
        print("=======")
        print(theme)
        papers = pc.get_papers_from_primary_theme(theme)
        print(len(papers))
        papers = pc.get_papers_from_secondary_theme(theme)
        print(len(papers))
    # papers = pc.get_papers_from_country('Canada')
    # for paper in papers:
    #     print(paper)
