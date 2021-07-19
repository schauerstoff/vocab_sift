import csv
from tkinter import Tk

# Copying a txt file row after row in your clipboard. use to put it in e.g. https://anacreondjt.gitlab.io/texthooker.html
# Manually go though list with yomichan and select your vocabulary!

data_path = 'res.txt'
kanji_pos = 0
english_pos = 1

r = Tk()
r.withdraw()

file = open(data_path)  # result from vocab_sift is not encoding='utf-8'
data = csv.reader(file, delimiter=",")

for row in data:
    r.clipboard_clear()
    print(row[kanji_pos] + '\t' + row[english_pos])
    r.clipboard_append(row[kanji_pos] + '\t' + row[english_pos])
    r.update()  # now it stays on the clipboard after the window is closed

file.close()
r.destroy()
