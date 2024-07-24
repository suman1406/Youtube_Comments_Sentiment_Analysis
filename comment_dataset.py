import os
import pandas as pd
from googleapiclient.discovery import build

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API')

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('http', '')
    text = text.replace('www', '')
    text = text.replace('https', '')
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    text = text.lower()
    return text

API_KEY = api_key
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_comments(video_id, max_results=100):
    comments = []
    results = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=max_results, textFormat='plainText').execute()
    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        if 'nextPageToken' in results:
            results = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=max_results, pageToken=results['nextPageToken'], textFormat='plainText').execute()
        else:
            break
    return comments

def get_video_id(url):
    if 'watch?v=' in url:
        video_id = url.split('watch?v=')[1]
        if '&' in video_id:
            video_id = video_id.split('&')[0]
        return video_id
    return None

video_url = "https://www.youtube.com/watch?v=VlvOgk5BHS4"
video_id = get_video_id(video_url)

if video_id:
    comments = get_comments(video_id)
    print(f"Fetched {len(comments)} comments from the video.")
    
    comments_df = pd.DataFrame(comments, columns=['comment'])
    comments_df.to_csv('youtube_comments.csv', index=False)
    print("Comments saved to youtube_comments.csv")
else:
    print("Invalid YouTube URL.")