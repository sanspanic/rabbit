import random
import hashlib
import time
import itertools

# minimum word length of words in phrase
# for retrieving 2nd anagram, change this to 2
MIN_WORD_LENGTH = 5
# number of words in phrase
NUM_OF_WORDS = 3
# for retrieving 2nd anagram, change this to "23170acc097c24edb98fc5488ab033fe"
HASH = "e4820b45d2277f3844eac66c903e84be"

with open("wordlist", "r") as f:
    wordlist = f.readlines()

# remove newline characters
filtered_words = []
for word in wordlist:
    new_word = word.replace("\n", "")
    filtered_words.append(new_word)

print("Total number of words: ", len(filtered_words))

# make dictionary of letter count for anagram
anagram = "poultryoutwitsants"
anagram_letter_count = {}
for letter in anagram:
    if letter in anagram_letter_count:
        anagram_letter_count[letter] += 1
    else:
        anagram_letter_count[letter] = 1

print("Anagram letter count: ", anagram_letter_count)

# eliminate words based on letters
correct_letters_only = []
for word in filtered_words:
    include = True
    # include only words of a certain length
    if len(word) < MIN_WORD_LENGTH:
        include = False
    # include only words without apostrophe
    if "'" in word:
        include = False
    for letter in word:
        if not letter in anagram_letter_count:
            include = False
    if include:
        correct_letters_only.append(word)

# eliminate words with incorrect amount of duplicate letters
no_duplicates = []
for word in correct_letters_only:
    include = True
    for key, val in anagram_letter_count.items():
        if val < word.count(key):
            include = False

    if include:
        no_duplicates.append(word)

print("Number of words after filtering: ", len(no_duplicates))

iters = itertools.permutations(no_duplicates, NUM_OF_WORDS)

found = False
while not found:
    word_combination = next(iters)

    if len(anagram) == len("".join(word_combination)):
        joined_phrase = " ".join(word_combination).encode()
        md5_hash = hashlib.md5(joined_phrase).hexdigest()
        if md5_hash == HASH:
            found = True


print("Result: ", word_combination)
