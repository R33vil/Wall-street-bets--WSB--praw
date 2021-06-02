import praw

reddit = praw.Reddit(client_id="FS524g1-1fR_1A",
                    client_secret="PW5CrOxQbvu6-2a9A6p_BWY2XNPQyQ",
                    username="python_praw_test001",
                    password="Jamesdaniel03!",
                    user_agent="pythonpraw")

subreddit =reddit.subreddit("wallstreetbets")

top_subreddit = subreddit.new(limit=500)

words_collection = []

for submission in top_subreddit:
    title = submission.title
    title_words =title.split()
    words_collection.append(title_words)

# print (words_collection)

# add words below between the '[]' this will specify what to appened from the output
potential_stocksymbols = []
known_not_stocks = ['UPVOTE', 'SUPPORT', 'YOLO', 'CLASS', 'ACTION', 'AGAINST', 'ROBINHOOD', 'GAIN',
                    'LOST', 'PORN', 'WSB', 'I', 'STILL', "DIDN'T", 'HEAR', 'NO', 'BELL', 'YOLO.', 'DD',
                    '200K', 'MOON!!!', 'MOON', 'WHAT', 'DEEPFUCKINGVALUE', 'PLAYERS', 'SELLERS', 'NOW']
for title in words_collection:
    for word in title:
        if word.isupper() and word not in known_not_stocks:
            potential_stocksymbols.append(word)

            print(potential_stocksymbols)

# for submission in top:
# print(submission.title)
