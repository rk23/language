last_depth = 0

# Recursively creates the database of words
def get_next(level, store, words, exclude=[]):
    word = words[level]

    if word in exclude or len(word) < 1:
        return

    if word not in store:
        store[word] = {
            'frequency': 1,
            'next': {}
        }
        return

    store[word]['frequency'] += 1

    if len(words) > level + 2:
        get_next(level + 1, store[word]['next'], words, exclude=exclude)

    return


# Recursively builds phrases and writes them to file
def write_word(next, phrase, total_frequency, depth, outfile, database, frequency_depth=10):
    if depth == 100:
        return

    if len(next) == 0:
        return

    sorted_next = sorted(next.items(),
                         key=lambda value: value[1]['frequency'],
                         reverse=True)
    if len(sorted_next) > 0:
        outfile.write("<ol>\n")

    depth += 1
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
        tf += database[word]['frequency']

        if phrase_frequency > frequency_depth:
            outfile.write("<li><span>" + (phrase + " " + word + " <i style='font-size:8px'>" + str(phrase_frequency)).strip() + "</i></span>" + "\n")

        write_word(next_word, phrase + " " + word, tf, depth, outfile, database, frequency_depth=frequency_depth)
    
    global last_depth
    last_depth = depth
    
    if len(sorted_next) > 0:
        outfile.write("</ol></li>\n")
    

def filter_input(text):
    return (text.lower()
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
         .replace('-', ' ')
         .replace(':', ' ')
         .replace('“', ' ')
         .replace("’ ", ' ')
         .replace('  ', ' ')
         .replace('http', ' ')
         .replace('https', ' ')
         .split(' '))