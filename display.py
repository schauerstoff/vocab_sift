import csv

# Creates html-code to display your results in display.html (paste below '<!-- INSERT DISPLAY.PY CODE HERE-->')
# Manually go though list with yomichan and select your new vocabulary!


data_path = 'anki1.txt'
kanji_pos = 0
english_pos = 1


new_words = []

file = open(data_path) 
data = csv.reader(file, delimiter="\t")


for row in data:
    print(row[english_pos] + '\t' + row[kanji_pos])
    # format: #"<div class="line_box"><span>あくび&nbsp;&nbsp; &nbsp;yawn</span></div>"
    new_words.append('<div class="line_box"><span>' +
                     row[kanji_pos] + '\t' + '\t' + '\t' + '&nbsp;&nbsp; &nbsp;' + '\t' + '\t' + '\t' + row[english_pos] + '</span></div>')

file.close()

# w writes strings, newline = '' => no newline
with open('display.txt', 'w') as out:
    for item in new_words:
        out.write("%s\n" % item)

#autom. einfuegen in html + oeffnen der seite moeglich?
