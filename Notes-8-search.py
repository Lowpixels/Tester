# Intro to Search
# Author: Marcus
# 25 November

import csv

# Introduction to Search Algorithms
# Search for all songs by "Kendrick"
# Display all YouTube and TikTok views
# Sort by either YouTube or TikTok views


def main():
    artist = "Kendrick Lamar"  # artist to find
    track_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)

        kendrick_songs = []

        # read each line of data
        for info in r:
            if artist == info[artist_col]:
                kendrick_songs.append(info)

        # print how many songs are in the list
        print(f"Number of Kendrick Songs: {len(kendrick_songs)}")

        # print our findings in a pretty way
        print("Track Name\t\tYouTube Views\t\tTikTok Views")  # header

        for song in kendrick_songs:
            current_track = song[track_col]
            current_ytviews = song[yt_views_col]
            current_tiktokviews = song[tiktok_views_col]

            print(f"{current_track}\t\t{current_ytviews}\t\t{current_tiktokviews}")


if __name__ == "__main__":
    main()
