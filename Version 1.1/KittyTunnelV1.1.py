from mowrikit import bc, clear
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress

while True:
#interface
    print("Built on PyTubeFix https://pypi.org/project/pytubefix/")
    print(bc.head+"KittyTunnel v1.1 by Mowrious\n"+bc.end)
    link = input(bc.bold+"Paste Youtube link here!"+bc.end+"\n: ")
    clear()
# Link-tracker removal
    sep = ['&si=','?si=']
    for x in sep:
        link = link.split(x, 1)[0]
        print(link)

# attempt to pull video and find right formating
    # SELECT FORMAT
    vidform = '0'
    while vidform == '0':
        print(bc.head + "Select Formating\n1.Highest Quality video .mp4\n2.Audio only .m4a\n3.Music Playlist pull" + bc.end + "\n")
        vidform = input(bc.bold+"Pick a format:"+bc.end+"\n: ")
        clear()
        # format the highest res video
        if vidform == '1':
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
        elif vidform == '2':
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
        elif vidform == '3':
            try:
                pl = Playlist(link)
                for video in pl.videos:
                    ys = video.streams.get_audio_only()
                    print(ys.title)
                    ys.download('./playlist')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!")
        else:
            vidform = '0'