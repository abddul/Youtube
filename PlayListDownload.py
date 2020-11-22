# dowanload pytube from github the pip version has a bug
# pip install git+https://github.com/nficano/pytube.git
import pytube


def sec2hm(time):
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return ("%d:%d:%d" % (hour, minutes, seconds))
def views(num):
    M =str(num)
    if len(M) >=7:
        
     return (M[0]+'.'+M[1]+' M')   
    if len(M)>=4 and len(M)<7:
      num=num/1000
      num=round(num)
      return str(num)+' K'
    if len(M)<=3:
        return num

url = input (" type URL :")
ytpl = pytube.Playlist(url)
print ("number of video of this list are: ",len(ytpl.video_urls))
total=0
for link in ytpl.video_urls:
    youtube=pytube.YouTube(link)
   # video = youtube.streams.get_highest_resolution()
    print ( youtube.title," video time =>",sec2hm(youtube.length) ,"rating => ",round(youtube.rating,1) ,"views =>",views(youtube.views))
    total+=youtube.length
print ("total time is", sec2hm(total) ,"hours")    

#video.download()
