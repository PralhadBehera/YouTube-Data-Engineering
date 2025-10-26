import requests
import json
import sys

Channel_Name = "RGBucketList"
API_KEY = "AIzaSyAFlqRjz20esEyeA4l1mR5HBfcBGQAWvo4"

API_URL = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,contentDetails&forHandle=@{Channel_Name}&key={API_KEY}"

def get_channel_info(url=API_URL):
    """Fetches data from the YouTube API and returns channel info as a dictionary."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('items'):
            channel_info = data['items'][0]

            # Extract channel details
            info = {
                "title": channel_info['snippet']['title'],
                "channel_id": channel_info['id'],
                "view_count": channel_info['statistics']['viewCount'],
                "subscriber_count": channel_info['statistics']['subscriberCount'],
                "video_count": channel_info['statistics']['videoCount'],
                "uploads_playlist_id": channel_info['contentDetails']['relatedPlaylists']['uploads']
            }

            return info
        else:
            print("Channel data not found in response.", file=sys.stderr)
            return None

    except Exception as e:
        print(f"Error fetching channel info: {e}", file=sys.stderr)
        return None


# if __name__ == "__main__":
#     info = get_channel_info()
#     if info:
#         print("\n--- Extracted Channel Details ---")
#         for k, v in info.items():
#             print(f"{k}: {v}")


info= get_channel_info()

if info:
    print("\n--- Extracted Channel Details ---")
    for k,v in info.items():
        print(f"{k}: {v}")


