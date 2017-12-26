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

for idx, _ in enumerate(words):
    get_next(idx, hash_table)

try:
    sorted_tuples = sorted(hash_table.items(),
                           key=lambda value: value[1]['frequency'],
                           reverse=False)
except Exception as e:
    print(e)
    sys.exit(1)

'''
next.items()
value['frequency']
'''


def print_word(next_tuple, phrase, frequency, depth):
    if depth == 5:
        return
    depth += 1
    for k, v in next_tuple.items():
        if frequency > 5 and v['frequency'] > 5:
            print(phrase + " " + k + " " + str(v['frequency']))

        spaces = "    " * depth

        print_word(v['next'], spaces + phrase + " " + k, v['frequency'], depth)


with open('output.txt', 'w') as outfile:
    for idx, _ in enumerate(sorted_tuples):
        i = sorted_tuples[idx]
        top_level_frequency = str(i[1]['frequency'])
        top_level_word = i[0]

        if top_level_frequency > 10:
            print(top_level_word + " " + top_level_frequency)

        print_word(i[1]['next'], "    " + top_level_word, top_level_frequency, 0)


            # for key, value in i[1]['next'].items():
        #     if value['frequency'] > 5:
        #         outfile.write("    " + top_level_word + " " + key + " " + str(
        #             value['frequency']) + "\n")
        #
        #     for ke, va in value['next'].items():
        #         if value['frequency'] > 5 and va['frequency'] > 1:
        #             outfile.write("        " + top_level_word + " " +
        #                 key + " " +
        #                 ke + " " +
        #                 str(va['frequency']) + "\n")
        #
        #         if va['next'] > 5:
        #             for k, v in va['next'].items():
        #                 if v['frequency'] > 1:
        #                     outfile.write("            " + top_level_word + " " +
        #                         key + " " +
        #                         ke + " " +
        #                         k + " " +
        #                         str(v['frequency']) + "\n")
        #
        #                 for x, y in v['next'].items():
        #                     if y['frequency'] > 0:
        #                         outfile.write("                " + top_level_word + " " +
        #                             key + " " +
        #                             ke + " " +
        #                             k + " " +
        #                             x + " " +
        #                             str(y['frequency']) + "\n")
        #
        #                     if y['next'] > 1:
        #                         for a, b in y['next'].items():
        #                             if b['frequency'] > 0:
        #                                 outfile.write("                    " + top_level_word + " " +
        #                                     key + " " +
        #                                     ke + " " +
        #                                     k + " " +
        #                                     x + " " +
        #                                     a + " " +
        #                                     str(b['frequency']) + "\n")


