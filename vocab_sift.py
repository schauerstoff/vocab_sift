import matplotlib.pyplot as plt
import csv

# Set your paths (.txt in UTF-8) and additional info (resp. columns, source)
# [relative path, column number for kanji]
data_paths = [
    ['database/mined.txt', 0],
    ['database/tobira.txt', 0],
    ['database/vn.txt', 0],
    ['database/genki.txt', 0]
]
# [relative path, column number for kanji, column number for english word, source name)]
new_data_paths = [
    ['newdata/N3Vocab1.txt', 0, 2, "1"],
    ['newdata/N3Vocab2.txt', 0, 4, "2"]
]

# test
# data_paths = [
#     ['database/testdata.txt', 0],
#     ['database/testdata2.txt', 1]
# ]
# # [relative path, column number for kanji, column number for english word, source name)]
# new_data_paths = [
#     ['newdata/newtestdata.txt', 1, 2, "tobira3"],
#     ['newdata/newtestdata2.txt', 1, 2, "tobira4"]
# ]

# how many words already in db, in every .txt
database_vocab_counters = [0] * len(data_paths)
# how many words in to-be-merged-lists, in every .txt
new_list_counters = [0] * len(new_data_paths)
# how many truly new vocab, in every .txt
new_vocab_counters = [0] * len(new_data_paths)

database = set()

# Read data and put them in set
for i in range(len(data_paths)):
    file = open(data_paths[i][0], encoding='utf-8')
    data = csv.reader(file, delimiter="\t")

    for row in data:
        # dict with only keys is called a set.
        database.add(row[data_paths[i][1]])
        database_vocab_counters[i] += 1

file.close()

# print(database)


new_words = []

# Read new data and compare them to the values in the set
# If not found, put them in list as Tupel (Kanji, English, Source)
for i in range(len(new_data_paths)):
    file = open(new_data_paths[i][0], encoding='utf-8')
    data = csv.reader(file, delimiter="\t")

    for row in data:
        #print(row[new_data_paths[i][1]], row[new_data_paths[i][2]], new_data_paths[i][3])
        tupel = (row[new_data_paths[i][1]],
                 row[new_data_paths[i][2]],
                 new_data_paths[i][3])
        new_list_counters[i] += 1
        if(not(tupel[0] in database)):
            new_words.append(tupel)
            # add to dictionary to avoid duplicates later
            database.add(tupel[0])
            new_vocab_counters[i] += 1


new_words.sort()
print(new_words)

# w writes strings, newline = '' => no newline
with open('res.txt', 'w',newline = '') as out:
    csv_out = csv.writer(out)
    for row in new_words:
        csv_out.writerow(row)


database_vocab_amount = sum(database_vocab_counters)
new_list_amount = sum(new_list_counters)
new_vocab_amount = sum(new_vocab_counters)

grundwert = database_vocab_amount + new_list_amount

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'anki already', 'to study', 'already studied from new words'
sizes = [database_vocab_amount, new_vocab_amount,
         new_list_amount-new_vocab_amount]
explode = (0, 0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


print(new_vocab_counters)
print(database_vocab_counters)

print(database_vocab_amount)
print(new_list_amount-new_vocab_amount)
print(new_vocab_amount)

plt.show()

# jetzt fehlt nur noch: go through list, put each row in clipboard, so it gets pasted to clipboard insert page.
# user can now manually add suitable vocabulary with yomichan!!

# def main():
#     pass


# if __name__ == '__main__':
#     main()
