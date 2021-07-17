import csv

# Set your paths (.txt in UTF-8) and additional info (resp. columns, source)
# [relative path, column number for kanji]
data_paths = [
    ['database/testdata.txt', 0],
    ['database/testdata2.txt', 1]
]
# [relative path, column number for kanji, column number for english word, source name)]
new_data_paths = [
    ['newdata/newtestdata.txt', 1, 2, "tobira3"]
]


database = set()

# Read data and put them in set
for i in range(len(data_paths)):
    file = open(data_paths[i][0], encoding='utf-8')
    data = csv.reader(file, delimiter="\t")

    for row in data:
        # dict with only keys is called a set.
        database.add(row[data_paths[i][1]])

file.close()

#print(database)


new_words = []

# Read new data and compare them to the values in the set
# If not found, put them in list as Tupel (Kanji, English, Source)
for i in range(len(new_data_paths)):
    file = open(new_data_paths[i][0], encoding='utf-8')
    data = csv.reader(file, delimiter="\t")

    for row in data:
        #print(row[new_data_paths[i][1]], row[new_data_paths[i][2]], new_data_paths[i][3])
        tupel = (row[new_data_paths[i][1]],
                 row[new_data_paths[i][2]], new_data_paths[i][3])
        if(not(tupel[0] in database)):
            new_words.append(tupel)

print(new_words)
new_words.sort()
print(new_words)


# def main():
#     pass


# if __name__ == '__main__':
#     main()
