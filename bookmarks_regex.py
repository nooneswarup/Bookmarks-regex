import re
import os


def remove_duplicates(x):
    return list(dict.fromkeys(x))


# boorkmarks.html consists of all the bookmarks you have. 
# if you have multiple bookmarks files, just concatinate them to one file and name it a bookmarks.html
with open("bookmarks.html", 'r', encoding="utf-8") as f:
    data = f.read()

match_first = re.findall(r'<A HREF=\".+?\"', data)
match_second = re.findall(r'>.[^>]+?<\/A>', data)

all_links = [i + j for i, j in zip(match_first, match_second)]
remove_duplicates = remove_duplicates(all_links)

print(os.getcwd())
with open('nodups.html', 'w', encoding="utf-8") as h:
    for item in remove_duplicates:
        h.write("<DT>%s" % item + "</DT>\n")
        
# nodups.html is the output file, all duplicates will be eliminated