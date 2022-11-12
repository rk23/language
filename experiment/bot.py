import praw
import requests
import json

r = praw.Reddit(user_agent='flowroute_engineers')
# r.set_oauth_app_info('rkapplication', '-hkw3tNSdyrnAf4sU8_FkLo5h_0', 'http://www.google.com')
subreddits = ('VOIP')

# with open('don_quixote.txt', 'a') as file:
for subreddit in subreddits:
    submissions = r.get_subreddit(subreddit).get_hot(limit=5)
    for sub in submissions:
        flat_comments = praw.helpers.flatten_tree(sub.comments)
        for comment in flat_comments:
            try:
                comment.body
            except Exception:
                break
            print(comment.body)
                # file.write(comment.body.lower().replace('\n', '').replace('.', '').replace(',', '').replace('?', '').replace('"', '').replace('-', '').split(' '))

# file.close()
