import praw
import csv
import os
from datetime import datetime

def authenticate():
    return praw.Reddit(
        client_id='nCJNw28iSSVNv5AkE1riTw',
        client_secret='LFXHQYI2i1nW3LRXiihP7OXxSFpgvQ',
        user_agent=True,
        username="BootDiscombobulated4", 
        password="thisaccountisonlyforfb365247"
    )

def scrape_posts(subreddit_name, sort_by="hot", limit=1000):
    reddit = authenticate()
    subreddit = reddit.subreddit(subreddit_name)
    posts = getattr(subreddit, sort_by)(limit=limit)

    data = []
    for idx, post in enumerate(posts, start=1):
        post.comments.replace_more(limit=0)  # Reduce API calls by not expanding comments
        top_comments = [comment.body for comment in post.comments[:20]]  # Top 20 comments

        data.append([
            idx,
            post.title,
            post.url,
            post.score,
            datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            post.num_comments,
            "|".join(top_comments),
            subreddit_name,
            post.id
        ])
        print(f"Processed post {idx}/{limit} from 'hot' in r/{subreddit_name}")
    
    return data

def save_to_csv(filename, headers, data):
    file_exists = os.path.isfile(filename)
    with open(filename, "a" if file_exists else "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)  # Write headers only if the file doesn't exist
        writer.writerows(data)

def scrape_subreddit_info(subreddit_name):
    reddit = authenticate()
    subreddit = reddit.subreddit(subreddit_name)

    data = [
        subreddit_name,
        datetime.fromtimestamp(subreddit.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
        subreddit.subscribers,
        subreddit.public_description
    ]
    return data

def main():
    subreddit_name = input("Enter subreddit name: ")

    # Scrape posts from 'hot'
    hot_posts_data = scrape_posts(subreddit_name, 'hot')
    save_to_csv(
        f"posts_hot_{subreddit_name}.csv",
        ["S.No", "Title", "URL", "Score", "Created_At", "Num_Comments", "Top_Comments", "Subreddit", "Post_ID"],
        hot_posts_data
    )
    print(f"Saved 'hot' posts to posts_hot_{subreddit_name}.csv")

    # Scrape subreddit info and save to subreddits.csv
    subreddit_info = scrape_subreddit_info(subreddit_name)
    save_to_csv(
        "subreddits.csv",
        ["Subreddit", "Created_At", "Subscribers", "Description"],
        [subreddit_info]
    )
    print(f"Updated subreddit info in subreddits.csv")

if __name__ == "__main__":
    main()
