import pandas as pd
from pytube import Playlist

# In this variable you need to replace the string message with the desired Youtube playlist URL
# URL of the YouTube playlist
playlist_url = "INSERT_YOUR_DESIRED_YOUTUBE_URL"

# Initialize a playlist object
playlist = Playlist(playlist_url)

# Create an empty list to store video details
video_details = []

# Loop through the videos in the playlist
for video in playlist.videos:
    # Extract video details using pytube
    title = video.title
    author = video.author
    video_url = video.watch_url
    views = video.views
    
    # Append the details to the list
    video_details.append([title, author, video_url, views])

# Create a DataFrame from the list of video details
columns = ["Title", "Author", "Video URL", "Views"]
df = pd.DataFrame(video_details, columns=columns)

# Sort the DataFrame by views in descending order
df = df.sort_values(by="Views", ascending=False)

# Select the top 10 videos based on views
top_10_df = df.head(10)

# Here you can change the name of the output file if desired
# Export the top 10 videos DataFrame to an Excel file
excel_file = "top_10_playlist.xlsx"
top_10_df.to_excel(excel_file, index=False, engine="openpyxl")

# This print message was made for the purpose of a YT tutorial video
# You can easily change the output if desired
print("An Excel file of the Top 10 videos in the playlist is now available, even though coding did all the work...")
