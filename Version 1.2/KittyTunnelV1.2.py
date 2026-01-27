from mowrikit import bc, clear, smenu
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress

while True:
#interface
    isurl = False
    while isurl is False:
        print(bc.bold+bc.blue+"Built on PyTubeFix under MIT licensing https://pypi.org/project/pytubefix/"+bc.end)
        print(bc.head+"KittyTunnel v1.2 by Mowrious\n"+bc.end)
        link = input(bc.bold+"Paste Youtube link here!\n: "+bc.end)
        if "https://" in link:
            isurl = True
        clear()
# Link-tracker removal
    sep = ['&si=','?si=']
    for x in sep:
        link = link.split(x, 1)[0]
    print(link)
    vidform = smenu(["yes","no"],"Download from Link? W, S and Enter to Select.")
    clear()
    if vidform == 0:
        if "playlist" in link:
            formats = ["Video Playlist","Audio only Playlist"]
            optshift = 3
        elif "watch" in link:
            formats = ["Highest quality Video","Audio only"]
            optshift = 1
        else:
            vidform = 1
            print(bc.red+"Invalid link!"+bc.end)
# attempt to pull video and find right formating
    # SELECT FORMAT

    while vidform == 0:
        vidform = smenu(formats, "Select Video Format using W, S and Enter.") + optshift
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