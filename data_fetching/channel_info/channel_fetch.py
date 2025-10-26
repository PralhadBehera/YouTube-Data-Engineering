import requests
import json
import sys

Channel_Name = "RGBucketList"

# The API URL you provided
API_URL = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,contentDetails&forHandle=@{Channel_Name}&key=AIzaSyAFlqRjz20esEyeA4l1mR5HBfcBGQAWvo4"

def fetch_and_print_channel_data(url):
    """Fetches data from the given YouTube API URL and prints the JSON response."""
    print("Fetching data from the YouTube Data API...")
    
    try:
        # Make the GET request to the API
        response = requests.get(url)
        
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status() 
        
        # Get the JSON data from the response
        data = response.json()
        
        print("\n--- Raw JSON Response ---")
        # Print the entire JSON response formatted with an indent
        print(json.dumps(data, indent=4))
        
        # --- Extract and print specific channel details ---
        
        # Check if the API returned any items
        if data.get('items'):
            channel_info = data['items'][0]
            
            # 1. Channel ID and Title
            channel_id = channel_info['id']
            title = channel_info['snippet']['title']
            
            # 2. Statistics
            stats = channel_info['statistics']
            view_count = stats['viewCount']
            subscriber_count = stats['subscriberCount']
            video_count = stats['videoCount']
            
            # 3. Uploads Playlist ID (for getting all videos)
            uploads_playlist_id = channel_info['contentDetails']['relatedPlaylists']['uploads']
            
            print("\n--- Extracted Channel Details ---")
            print(f"Channel Name: {title}")
            print(f"Channel ID: {channel_id}")
            print(f"Total Views: {view_count}")
            print(f"Subscribers: {subscriber_count}")
            print(f"Video Count: {video_count}")
            print(f"Uploads Playlist ID: {uploads_playlist_id}")
            
        else:
            print("\nError: Channel data not found in the response (items list is empty).")
            
    except requests.exceptions.HTTPError as errh:
        print(f"\nHTTP Error occurred: {errh}", file=sys.stderr)
    except requests.exceptions.ConnectionError as errc:
        print(f"\nError Connecting: {errc}", file=sys.stderr)
    except requests.exceptions.Timeout as errt:
        print(f"\nTimeout Error: {errt}", file=sys.stderr)
    except requests.exceptions.RequestException as err:
        print(f"\nAn unexpected error occurred: {err}", file=sys.stderr)
    except Exception as e:
        print(f"\nAn error occurred while processing the data: {e}", file=sys.stderr)

if __name__ == "__main__":
    fetch_and_print_channel_data(API_URL)
    


