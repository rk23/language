# Language learning by pareto principle

The application in this repo creates an `index.html` file that can be used to navigate the most frequent words and phrases from a supplied body of text. 

To generate the html file, in `app/` run 

`python3 app.py` 

and open the html file

`open index.html`

There will be a list of single words ordered by frequency. Clicking a word will open the next level of associated phrases with that word to the depth specified. It's recommended to not have too low of a depth as this will affect performance especially with larger bodies of text.

## Intent

This is a tool to help language learners find important vocabulary to study. The idea is backed by the Pareto Principle: 20% of the words in a text give 80% of it's understanding. To prove this principle, data analysis was done on a sample text of over 15,000 words from The Count of Monte Cristo in the original French - 20.02% of the unique words accounted for 79.68% of the total words in the text.

By studying top-down through this list by frequency, the most frequent words are more strongly reinforced and less time is spent on memorizing rarely used conjugations. Also, one of the best benefits is finding and learning frequently used phrases that have different meanings than the individual words in isolation. "For example" is a good example itself - "for" and "example" have independent meanings that aren't intuitive to put together by a student of English but the meaning makes sense when learned as a phrase.

### TODO
- Google translate button next to every word / phrase
- Toggle open / collapse all
- Input for frequency depth
- Frontend input for text
