import json
import sys

hash_table = {}

with open('source.txt', 'r') as myfile:
    text = myfile.read()
words = (text.lower()
         .replace('\n', ' ')
         .replace('.', ' ')
         .replace(',', ' ')
         .replace("'", ' ')
         .replace('?', ' ')
         .replace('"', ' ')
         .replace(';', ' ')
         .replace(':', ' ')
         .replace('-', ' ')
         .replace('  ', ' ')
         .split(' '))

not_tracked = ['the', 'and', 'of', 'to', 'in', 'that']
# not_tracked = []

total = len(words)


def get_next(level, store, repass=False):
    word = words[level]

    if word in not_tracked:
        return
    if len(word) < 1:
        return
    if word not in store:
        store[word] = {
            'frequency': 1,
            'next': {}
        }
        return
    if not repass:
        store[word]['frequency'] += 1
    if len(words) > level + 2:
        get_next(level + 1, store[word]['next'], repass=repass)
    return


def print_word(next_tuple, phrase, frequency, depth, outfile):

    if depth == 5:
        return

    depth += 1

    for k, v in next_tuple.items():
        if frequency > 5 and v['frequency'] > 5:
            outfile.write(phrase + " " +
                  k + " " +
                  str(v['frequency']) + "\n")

        spaces = "    " * depth

        print_word(v['next'], spaces + phrase + " " + k, v['frequency'], depth, outfile)


for idx, _ in enumerate(words):
    get_next(idx, hash_table)

try:
    sorted_tuples = sorted(hash_table.items(),
                           key=lambda value: value[1]['frequency'],
                           reverse=True)
except Exception as e:
    print(e)
    sys.exit(1)


with open('output.txt', 'w') as outfile:
    for idx, _ in enumerate(sorted_tuples):
        i = sorted_tuples[idx]
        top_level_frequency = str(i[1]['frequency'])
        top_level_word = i[0]

        if top_level_frequency > 10:
            outfile.write((top_level_word + " " + top_level_frequency) + "\n")

        print_word(i[1]['next'], "    " + top_level_word, top_level_frequency, 0, outfile)
