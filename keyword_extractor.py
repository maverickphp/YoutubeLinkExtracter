import os
import google.auth
import google.auth.transport.requests
import requests
from google.oauth2.credentials import Credentials

# Set up the YouTube API client
from googleapiclient.discovery import build
DEVELOPER_KEY = "YOUR_API_KEY_FROM_GOOGLE_API_YOUTUBE_DATA"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

# Define the search query
query = "roboloxgamesbloxburg"

# Execute the search and extract the video URLs
video_urls = []
search_response = youtube.search().list(
    q=query,
    type="video",
    part="id",
    maxResults=55
).execute()
for search_result in search_response.get("items", []):
    video_urls.append(f"https://www.youtube.com/watch?v={search_result['id']['videoId']}")

# Write the video URLs to a text file
with open("bloxburg_videos9.txt", "w") as f:
    for video_url in video_urls:
        f.write(video_url + "\n")
