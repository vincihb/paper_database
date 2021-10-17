import random
import time

from amr_categories.Animals import Animals
from amr_categories.CleanWater import CleanWater
from amr_categories.Environment import Environment
from amr_categories.FoodSafety import FoodSafety
from amr_categories.HumanConsumption import HumanConsumption
from amr_categories.HumanIPC import HumanIPC
from amr_categories.Plants import Plants
from amr_categories.RAndD import RAndD
from data.PaperCache import PaperCache
from multiprocessing import Process


def populate_parallel(pc, paper_id, themes_class_dict):
    theme_dict = {'ipc': 0, 'consumption': 0, 'water': 0, 'environment': 0, 'food': 0, 'animals': 0,
                  'plants': 0, 'randd': 0}
    for key in themes_class_dict.keys():
        theme_dict.update({key: themes_class_dict.get(key).get_weighting_theme_from_paper_id(paper_id)})
    sorted_themes = list(dict(sorted(theme_dict.items(), key=lambda x: x[1], reverse=True)).keys())
    if int(paper_id) % 100 == 0:
        print(paper_id)
    primary_theme = sorted_themes[0]
    secondary_theme = sorted_themes[1]
    pc.update_theme(paper_id, primary_theme, secondary_theme)


def kth_nn(theme, pc):
    theme.set_all_papers_primary_database()
    all_papers = theme.all_papers
    new_keywords = {}
    for paper in all_papers:
        keywords = pc.get_keywords_from_paper_id(paper.get('ID'))
        for keyword in keywords:
            if new_keywords.get(keyword.get('KEYWORD')) is None:
                new_keywords.update({keyword.get('KEYWORD'): keyword.get('WEIGHT')})
            else:
                new_keywords.update({keyword.get('KEYWORD'): keyword.get('WEIGHT')
                                                             + new_keywords.get(keyword.get('KEYWORD'))})
    new_keywords = list(dict(sorted(new_keywords.items(), key=lambda x: x[1], reverse=True)).keys())[:100]
    return new_keywords


def populate_theme():
    pc = PaperCache()
    all_papers = pc.get_all_papers()
    themes = {'ipc': HumanIPC(), 'consumption': HumanConsumption(),
              'water': CleanWater(), 'environment': Environment(),
              'food': FoodSafety(), 'animals': Animals(), 'plants': Plants(),
              'randd': RAndD()}
    processes = []
    index = 0
    process_num = 40
    prev_keywords = {k: themes.get(k).theme_keywords for k in themes.keys()}
    print(prev_keywords)
    new_keywords = {k: kth_nn(themes.get(k), pc) for k in themes.keys()}
    for key in new_keywords.keys():
        print(key)
        print(new_keywords.get(key))
    exit()
    prev_time = [1000000]
    start_time = time.time()
    for paper in all_papers:
        populate_parallel(pc, paper.get('ID'), themes)
        p = Process(target=populate_parallel, args=(pc, paper.get('ID'), themes))
        p.start()
        processes.append(p)
        index = index + 1
        if index % process_num == 0:
            index = 0
            for process in processes:
                process.join()
            elapsed_time = time.time() - start_time
            if float(elapsed_time) / float(process_num) <= min(prev_time) or random.randrange(0, 2) == 1:
                process_num += 1
            else:
                process_num -= 1
            prev_time = [min(prev_time), float(elapsed_time) / float(process_num)]
            start_time = time.time()
            print(process_num)
            processes = []


populate_theme()
