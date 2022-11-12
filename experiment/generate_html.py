import matplotlib.pyplot as plt

from decimal import Decimal

hash_table = {}
SPACES = "  "
x = []
y = []

efficiency = []


def get_next(level, store):
    word = words[level]

    if word in not_tracked or len(word) < 1:
        return

    if word not in store:
        store[word] = {
            'frequency': 1,
            'next': {}
        }
        return

    store[word]['frequency'] += 1

    if len(words) > level + 2:
        get_next(level + 1, store[word]['next'])

    return


def print_word(next_tuple, phrase, total_frequency, depth, outfile):
    if depth == 100:
        return

    sorted_next = sorted(next_tuple.items(),
                         key=lambda value: value[1]['frequency'],
                         reverse=True)

    depth += 1
    if depth == 1:
       outfile.write("<ol>\n")
    for index, _ in enumerate(sorted_next):
        word_object = sorted_next[index]

        word = word_object[0]
        phrase_frequency = word_object[1]['frequency']
        next_word = word_object[1]['next']

        # The idea here is that you are learning each word in the phrase
        # independently, so add up the frequencies of all individual words
        # then add the phrase frequency because the phrase is itself a sign.
        # Problem is duplicates. Can't just graph this.
        tf = total_frequency + phrase_frequency
        tf += hash_table[word]['frequency']

        if phrase_frequency > 0:
            efficiency.append(((phrase + " " + word).replace('  ', ''), phrase_frequency))
            opt = "<li><span>" + phrase + " " + word + " " + str(phrase_frequency) + "</span>" + "\n"
            outfile.write(opt)
        else:
            continue
        # spaces = SPACES * depth
        print_word(next_word, opt, tf, depth, outfile)
        
        if depth == len(sorted_tuples) - 1:
            outfile.write("</ol>\n")

with open('./data/source.txt', 'r') as myfile:
    text = myfile.read()
words = (text.lower()
         .replace('\n', ' ')
         .replace('.', ' ')
         .replace(',', ' ')
         .replace("—", ' ')
         .replace('”', ' ')
         .replace('(', ' ')
         .replace(')', ' ')
         .replace('"', ' ')
         .replace(';', ' ')
         .replace('_', ' ')
         .replace(':', ' ')
         .replace('“', ' ')
         .replace('  ', ' ')
         .split(' '))

not_tracked = ['the', 'and', 'of', 'to', 'in', 'that']

total = len(words)

for idx, _ in enumerate(words):
    get_next(idx, hash_table)

sorted_tuples = sorted(hash_table.items(),
                       key=lambda value: value[1]['frequency'],
                       reverse=True)

# import json
# print(json.dumps(dict(sorted_tuples)))

with open('output.txt', 'w') as outfile:
    for idx, _ in enumerate(sorted_tuples):
        i = sorted_tuples[idx]
        top_level_frequency = i[1]['frequency']
        top_level_word = i[0]

        x_percent = (Decimal(idx) / Decimal(len(sorted_tuples))) * Decimal(100)
        x_literal = idx

        x.append(x_literal)
        y.append(top_level_frequency)

        if top_level_frequency > 1:
            outfile.write(("<li><span>" + top_level_word + " " + str(top_level_frequency) + "</span>") + "\n")

        print_word(i[1]['next'], top_level_word, top_level_frequency, 0, outfile)

