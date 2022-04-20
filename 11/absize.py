import sys
import re
# A complete token is a word if:
# - it consists entirely of characters a-z, A-Z, and ' (apostrophe), and
# - there is at most one character from A-Z and if it exists it occurs first, and
# - there is at most one apostrophe that does not occur first
# The word it represents is its lower case form, including the apostrophe if present.
# A token contains a word if it is of the form <a><b><c> where:
# <a> is empty or a double quote character (")
# <b> is a word as above
# <c> is empty or a single character which is a punctuation symbol (. , ; : ? !) or a double quote character.
# Then, of course, <b> is the word it contains.
# Note we do want to allow, e.g.,
# "To
# to contain the word 'to' since it might be the beginning of a longer quote "To be or not to be".


"""
Input and Task Decision
If valid add to set then print sorted words.
example input: "Hello World 4312i"
"""
word_set = set()
for line in sys.stdin:
    input = line.strip()
    if input:  # Python trick - empty strings are 'false'
        x = re.split('[\s]', input)
        # x is an array of words on a line
        for word in x:
            word_check = re.findall('\"?[A-Z]?[a-z]*\'?[a-z]*[.,;:?!"]?$', word)
            if word_check[0] == word and word:
                if not (word[-1].isalpha() or word[-1] == '\''):
                    # print(word[-1])
                    word = word[:-1]
                if word:
                    if not (word[0].isalpha()):
                        word = word[1:]
                if word:
                    word_set.add(word.lower())
word_list = list(word_set)
word_list.sort()
for i in word_list:
    print(i)
