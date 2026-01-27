from mowrikit import bc, clear, smenu
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress


while True:

#interface
    isurl = False

#insert link menu/home
    while not isurl:
        print(bc.bold+bc.blue+"Built on PyTubeFix under MIT licensing https://github.com/juanbindez/pytubefix"+bc.end)
        print(bc.head+"KittyTunnel v1.3 by Mowrious\n"+bc.end)
        link = input(bc.bold+"Paste Youtube link here!\n: "+bc.end)

        if "https://" in link:
            isurl = True
        clear()

# Link-tracker removal
    sep = ['&si=','?si=']
    for x in sep:
        link = link.split(x, 1)[0]

# confirm download
    vidform = smenu(["yes","no"],"W=up, S=down and Enter=confirm to Select.","Shortened link: "+link+"\nDo you want to download from this Link?")
    clear()

#checking to confirm link is youtube
    if vidform == 0:
        if "youtu.be" or "youtube.com" in link:
            formats = ["Highest quality Video","Audio only"]
            optshift = 1
        elif "playlist" in link:
            formats = ["Video Playlist","Audio only Playlist"]
            optshift = 3
        elif "short" in link:
            formats = ["Highest quality Video","Audio only"]
            optshift = 1
        else:
            vidform = 1
            print(bc.red+"Invalid link!"+bc.end)

# attempt to pull video and find right formating
    # SELECT FORMAT
    while vidform == 0:
        vidform = smenu(formats, "W=up, S=down and Enter=confirm to Select.","Select the download format you want.") + optshift
        clear()
        # format the highest res video
        if vidform == 1:
            try:
                youtubeObject = YouTube(link, on_progress_callback=on_progress)
                youtubeObject = youtubeObject.streams.get_highest_resolution()
                print(youtubeObject.title)
                youtubeObject.download('./video')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!")
        # format audio only
        elif vidform == 2:
            try:
                youtubeObject = YouTube(link, on_progress_callback=on_progress)
                youtubeObject = youtubeObject.streams.get_audio_only()
                print(youtubeObject.title)
                youtubeObject.download('./audio')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!")
        # format to a playlist
        elif vidform == 3:
            try:
                pl = Playlist(link)
                for video in pl.videos:
                    ys = video.streams.get_highest_resolution()
                    print(ys.title)
                    ys.download('./video_playlist')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!")
        # format to a audio playlist
        elif vidform == 4:
            try:
                pl = Playlist(link)
                for video in pl.videos:
                    ys = video.streams.get_audio_only()
                    print(ys.title)
                    ys.download('./audio_playlist')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!")
        else:
            vidform = 0