import json
import sys

hash_table = {}


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
    if depth == 10:
        return

    sorted_next = sorted(next_tuple.items(),
                    key=lambda value: value[1]['frequency'],
                    reverse=True)

    depth += 1
    for index, _ in enumerate(sorted_next):
        word_object = sorted_next[index]
        word = word_object[0]
        freq = word_object[1]['frequency']
        next_word = word_object[1]['next']
        if frequency > 1 and freq > 1:
            outfile.write(phrase + " " +
                  word + " " +
                  str(freq) + "\n")
        spaces = "    " * depth

        print_word(next_word, spaces + phrase + " " + word, str(freq), depth, outfile)


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

total = len(words)
print("Total words parsed: {}".format(total))


for idx, _ in enumerate(words):
    get_next(idx, hash_table)

sorted_tuples = sorted(hash_table.items(),
                       key=lambda value: value[1]['frequency'],
                       reverse=True)

with open('output.txt', 'w') as outfile:
    for idx, _ in enumerate(sorted_tuples):
        i = sorted_tuples[idx]
        top_level_frequency = str(i[1]['frequency'])
        top_level_word = i[0]

        if top_level_frequency > 10:
            outfile.write((top_level_word + " " + top_level_frequency) + "\n")

        print_word(i[1]['next'], "    " + top_level_word, top_level_frequency, 0, outfile)
