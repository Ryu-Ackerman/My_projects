import yt_dlp as yd

def video_downloader(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]',
        'nonplaylist': True
    }
    with yd.YoutubeDL(ydl_opts) as somth:
        somth.download([url])

if __name__ == '__main__':
    url = input('Enter the url: ')
    video_downloader(url)

