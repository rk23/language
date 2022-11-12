SPACES = "  "
FREQUENCY_DEPTH = 10

last_depth = 0
hash_table = {}
not_tracked = ['the', 'and', 'of', 'to', 'in', 'that']


# Recursively creates the database of words
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


# Recursively builds phrases and writes them to file
def write_word(next, phrase, total_frequency, depth, outfile):
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
        tf += hash_table[word]['frequency']

        if phrase_frequency > FREQUENCY_DEPTH:
            outfile.write("<li><span>" + (phrase + " " + word + " <i style='font-size:8px'>" + str(phrase_frequency)).strip() + "</i></span>" + "\n")

        write_word(next_word, phrase + " " + word, tf, depth, outfile)
    
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


with open('./data/portuguese.txt', 'r') as myfile:
    text = myfile.read()

words = filter_input(text)
total = len(words)

for idx, _ in enumerate(words):
    get_next(idx, hash_table)

sorted_words = sorted(hash_table.items(),
                       key=lambda value: value[1]['frequency'],
                       reverse=True)


with open('index.html', 'w') as outfile:
    outfile.write('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script type="text/javascript" src="/Users/reedk/src/language/app/resources/js/source.js"></script>
    <link rel="stylesheet" href="resources/css/bootstrap.css">
    <link rel="stylesheet" href="resources/css/app.css"> 
    <style type="text/css">
    </style>
</head>

<body>
    <div class="container">
    <h1>Language Learning</h1>
    <div class="row">
    <div class="col-4">
    </div>
    <div class="col-8">
    <ol class="col_ol" style="margin-top: 10%">
    ''')
    try:
        for idx, _ in enumerate(sorted_words):
            i = sorted_words[idx]
            top_level_frequency = i[1]['frequency']
            top_level_word = i[0]

            if top_level_frequency > 10:
                outfile.write("<li><span>" + top_level_word + " <i style='font-size:8px'>" + str(top_level_frequency) + "</i></span>" + "\n")
                write_word(i[1]['next'], SPACES + top_level_word, top_level_frequency, 0, outfile)
    except Exception as e:
        print(e)
    outfile.write("""
        </ol>
        </div>
        </div>
</body>

</html>
    """)
