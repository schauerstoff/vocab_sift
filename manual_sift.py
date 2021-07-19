import csv
from shutil import copyfile
import shutil


# Manually sift through res.txt (created with automatic_sift.py) and decide what to do with each word!
data_path = 'res.txt'
kanji_pos = 0
english_pos = 1

copyfile('res.txt', 'res_workingcopy.txt')
anki = []
later = []
#later = open('results/later.txt', 'w')
#anki = open('results/anki.txt', 'w')

file = open('res_workingcopy.txt')
res = csv.reader(file, delimiter=",")
columns = shutil.get_terminal_size().columns

for row in res:
    word = row[kanji_pos] + '\t' + row[english_pos]
    print("_________________________________________\n".center(columns))
    
    print(word.center(columns))
    switch = input ("") #Later -> l \n Anki -> a \n Drop -> d

    if(switch == "l"):
        print("added to later.txt".center(columns))
        later.append(word)
        #later.write("%s\n" % word)
    elif(switch == "a"):
        print("ankified".center(columns))
        anki.append(word)
        #anki.write("%s\n" % word)
    elif(switch == "d"):
        print("dropped".center(columns))
        #remove from workingcopy

        # Write to anki.txt
    with open('results/anki.txt', 'w') as out:
        for item in anki:
            out.write("%s\n" % item)

    # Write to later.txt
    with open('results/later.txt', 'w') as out:
        for item in later:
            out.write("%s\n" % item)
    print("_________________________________________".center(columns))
    print("\n \n \n \n \n")

file.close()

#safer to do this as you go
# # Write to anki.txt
# with open('results/anki.txt', 'w') as out:
#     for item in anki:
#         out.write("%s\n" % item)

# # Write to later.txt
# with open('results/later.txt', 'w') as out:
#     for item in later:
#         out.write("%s\n" % item)
