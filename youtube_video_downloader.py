#!/usr/bin/env python3

from pytube import YouTube
from pytube.exceptions import RegexMatchError
import sys

# ANSI escape codes for colored output.
BLUE = "\033[94m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
YELLOW = "\033[93m"

RESET = "\033[0m"


def progress_bar(stream, chunk, bytes_remaining):
    """
    Display a progress bar for the video download.

    Args:
        stream (Stream): the stream being downloaded.
        chunk (bytes): the chunk of data that was just downloaded.
        bytes_remaining (int): the number of bytes remaining to be downloaded.
    """
    total_size = stream.filesize
    downloaded = total_size - bytes_remaining
    progress = int(downloaded / total_size * 50)
    sys.stdout.write("\r[{}{}{}{}] {:.2f}% ".format(MAGENTA, "=" * progress, RESET, " " * (50 - progress), downloaded / total_size * 100))
    sys.stdout.flush()


def download_video(video_url):
    """
    Download the highest resolution of a YouTube video.

    Args:
        video_url (str): the URL of the YouTube video to download.

    Raises:
        RegexMatchError: if the video URL does not match the expected pattern.
    """
    try:
        yt = YouTube(video_url, on_progress_callback=progress_bar)
        stream = yt.streams.get_highest_resolution()
        filename = f"{yt.author} - {yt.title}.mp4"
        stream.download(filename=filename)
        print(f"\n{GREEN}Download complete.{RESET}\n")
    except RegexMatchError:
        print(f"{RED}ERROR: could not match regex for video ID.{RESET}\n")


def main():
    """
    Main function to prompt the user for a YouTube video URL and download it.
    """
    print(f"\n{YELLOW}YOUTUBE VIDEO DOWNLOADER")
    print("=" * 24)

    video_url = input(f"\n{RESET}Enter the YouTube video URL to download: ")
    download_video(video_url)


if __name__ == "__main__":
    main()
