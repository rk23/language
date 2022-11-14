from functions import filter_input, get_next, write_word

SPACES = "  "
FREQUENCY_DEPTH = 10

database = {}
exclusion_list = ['the', 'and', 'of', 'to', 'in', 'that']

with open('./data/alchemist.txt', 'r') as myfile:
    text = myfile.read()

words = filter_input(text)
total = len(words)

for idx, _ in enumerate(words):
    get_next(idx, database, words, exclude=exclusion_list)

sorted_words = sorted(database.items(),
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
                write_word(i[1]['next'], SPACES + top_level_word, top_level_frequency, 0, outfile, database, frequency_depth=FREQUENCY_DEPTH)
    except Exception as e:
        print(e)
    outfile.write("""
        </ol>
        </div>
        </div>
</body>

</html>
    """)
