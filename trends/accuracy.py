import random

from data.PaperCache import PaperCache

a = PaperCache()
# a.set_all_papers_primary_database()
papers = a.get_all_papers()
n = (1.96/0.05)**2*0.25
sample_size = (len(papers) * n)/(len(papers) + n)
print("Sample size: " + str(round(sample_size, 0)))
print("Total: " + str(len(papers)))
sample = random.sample(papers, 373)
accuracy_array = []
index = 0
for s in sample:
    print(index)
    index = index + 1
    print(s.get('TITLE'))
    print(s.get('ABSTRACT'))
    print("Primary theme is: " + a.get_paper_theme(s.get('ID'))[0].get('PRIMARY_THEME'))
    print("Secondary theme is: " + a.get_paper_theme(s.get('ID'))[0].get('SECONDARY_THEME'))
    while True:
        try:
            accuracy_array.append(int(input("Correctly identified primary and secondary themes? ")))
            break
        except ValueError:
            print("Please enter integer 0, 1: ")
            print("Accuracy estimate: " + str(sum(accuracy_array) / len(accuracy_array)))
print("Accuracy estimate: " + str(sum(accuracy_array) / len(accuracy_array)))
# print("====")
# print("Secondary Theme papers sample")
# accuracy_array = []
# a.set_all_papers_secondary_database()
# papers = a.all_papers
# sample = random.sample(papers, 94)
# print("Total: " + str(len(papers)))
# for s in sample:
#     print(s.get('TITLE'))
#     print(s.get('ABSTRACT'))
#     while True:
#         try:
#             accuracy_array.append(int(input("Secondary theme? ")))
#             break
#         except ValueError:
#             print("Please enter integer 0, 1: ")
#             print("Accuracy estimate: " + str(sum(accuracy_array) / len(accuracy_array)))
