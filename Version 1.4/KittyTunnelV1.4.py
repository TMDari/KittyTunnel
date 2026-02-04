from mowrikit import bc, clear, smenu
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from sys import exc_info

optshift = 0
link = ""
formats = []

def downytv(thelink):
    list_of_clients = ['WEB', 'WEB_EMBED', 'WEB_MUSIC', 'WEB_CREATOR', 'WEB_SAFARI', 'ANDROID', 'ANDROID_MUSIC', 'ANDROID_CREATOR', 'ANDROID_VR', 'ANDROID_PRODUCER', 'ANDROID_TESTSUITE', 'IOS', 'IOS_MUSIC', 'IOS_CREATOR', 'MWEB', 'TV', 'TV_EMBED', 'MEDIA_CONNECT']
    success = False
    for client in list_of_clients:
        if not success:
            try:
                ytube = YouTube(thelink, client=client)
                stream = ytube.streams.get_by_itag(140)
                print(ytube.title)
                stream.download('./video')
            except:
                error_type, err, error_traceback = exc_info()
                print(f'Failed client: {client} with Error: {err}\n')
            else:
                print(f'Success with client {client}\nsaved to ./video\n')
                success = True


while True:

#interface
    isurl = False
#insert link menu/home
    while not isurl:
        print(bc.bold+bc.blue+"Built on PyTubeFix under MIT licensing https://github.com/juanbindez/pytubefix"+bc.end)
        print(bc.head+"KittyTunnel v1.4 by Mowrious\n"+bc.end)
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

#checking to confirm link is YouTube
    if vidform == 0:
        if "youtu.be" or "youtube.com" in link:
            formats = ["Highest quality Video","try all clients (experimental)","Pick one by choice (experimental)","Audio only"]
            optshift = 1
        elif "short" in link:
            formats = ["Highest quality Video","Audio only"]
            optshift = 1
        else:
            vidform = 1
            print(bc.red+"Invalid link!"+bc.end)
        if "playlist" in link and vidform == 0:
            formats = ["Video Playlist","Audio only Playlist"]
            optshift = 5

# attempt to pull video and find right formating
    # SELECT FORMAT
    while vidform == 0:
        vidform = smenu(formats, "W=up, S=down and Enter=confirm to Select.","Select the download format you want.") + optshift
        clear()
        # format the highest res video
        if vidform == 1:
            try:
                yt = YouTube(link, on_progress_callback=on_progress)
                yt = yt.streams.get_highest_resolution()
                print(yt.title)
                yt.download('./video')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!\nsaved to ./video")
        # attempt to pull video with all clients
        elif vidform == 2:
            downytv(link)
        # advanced option, user selects download format. experimental and unstable
        elif vidform == 3:
            try:
                yt = YouTube(link, on_progress_callback=on_progress)
                ytpull= smenu(yt.streams, "W=up, S=down and Enter=confirm to Select.", "Pick a stream to pull")
                yt = yt.streams[int(ytpull)]
                print(yt.title)
                yt.download('./video')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!\nsaved to ./video")
        # format audio only
        elif vidform == 4:
            try:
                yt = YouTube(link, on_progress_callback=on_progress)
                yt = yt.streams.get_audio_only()
                print(yt.title)
                yt.download('./audio')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!\nsaved to ./audio")
        # format to a playlist
        elif vidform == 5:
            try:
                pl = Playlist(link)
                for video in pl.videos:
                    ys = video.streams.get_highest_resolution()
                    print(ys.title)
                    ys.download('./video_playlist')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!\nsaved to ./video_playlist")
        # format to an audio playlist
        elif vidform == 6:
            try:
                pl = Playlist(link)
                for video in pl.videos:
                    ys = video.streams.get_audio_only()
                    print(ys.title)
                    ys.download('./audio_playlist')
            except Exception as e:
                print("ERROR: ", e)
            else:
                print("Download finished!\nsaved to ./audio_playlist")
        else:
            vidform = 0