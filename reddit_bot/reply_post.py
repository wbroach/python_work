import praw
import re
import os

def make_reply_hot(botname, username, subreddit, search_term, reply, posts=200, 
    file_record="posts_replied_to.txt", reply_nested_comments=False):
    
    # Create the Reddit instance
    reddit = praw.Reddit(botname)
    post_count = 0

    # and login
    # not necessary if .init file is correctly entered
    #reddit.login(REDDIT_USERNAME, REDDIT_PASS)

    # Have we run this code before? If not, create an empty list
    if not os.path.isfile(file_record):
        posts_replied_to = []

    # If we have run the code before, load the list of posts we have replied to
    else:
        # Read the file into a list and remove any empty values
        with open(file_record, "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    # Get the top 5 values from our subreddit
    subreddit = reddit.subreddit(subreddit)
    for submission in subreddit.hot(limit=posts):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            if re.search(search_term, submission.title, re.IGNORECASE) or re.search(search_term, submission.selftext, re.IGNORECASE):
                # Reply to the post
                submission.reply(reply)
                print("Bot replying to : " + str(submission.title) + " in r/" + str(subreddit) + ".")
                post_count += 1
                # Store the current id into our list
                posts_replied_to.append(submission.id)
                
            # Reply to comments
            submission.comments.replace_more(limit=0)
            comment_queue = submission.comments[:]
            while comment_queue:
                comment = comment_queue.pop(0)
                author = comment.author.name
                
                if re.search(search_term, comment.body, re.IGNORECASE) and author != username:
                    comment.reply(reply)
                    print("Replied to comment in submission: " + str(submission.id) + "in r/" + str(subreddit) + ".")
                    post_count += 1
                    posts_replied_to.append(submission.id)
                
                if reply_nested_comments:
                    comment_queue.extend(comment.replies)
                
    if post_count < 1:
        print("No new postings to " + "r/" + str(subreddit) + ".")

    # Write the updated list back to the file
    with open(file_record, "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


# Sample main below
bot_info = {'dippingtobacco' : 
                {'bot name' : 'bot1', 
                'search term' : 'peach', 
                'reply term' : "Skoal. Fuckin'. PEACH!!!!!"
                },
            'SKOALFUCKINPEACH' :
                {'bot name' : 'bot1', 
                'search term' : 'peach', 
                'reply term' : "Skoal. Fuckin'. PEACH!!!!!"
                }
           }
           
for k in bot_info.keys():
    make_reply_hot(bot_info[k]['bot name'], 'RKFluffy_Bot',k, bot_info[k]['search term'], bot_info[k]['reply term'], posts=25)
