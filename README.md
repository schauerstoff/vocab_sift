# vocab_sift
Compare lists of new words to your database and sift out all the duplicates!

Useful for:
    - merging anki decks
    - comparing your vocabulary to a vocabulary list (e.g. for test-preparation-purposes) and get stats displayed

Consists of:
    1. automatic_sift.py:  returns {∀ word ∈ {vocabulary_list} | ¬ (word ∈ {database})}
    2. manual_sift.py:  Use the result from 1. to manually sort the rest in three categories
                        - Study (and add to Anki)
                        - Later (low hanging fruit only)
                        - Drop (e.g. when word is already known)

#stats: how many new kanji mayb
