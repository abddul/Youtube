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
totaltime=0
totalviews=0
for link in ytpl.video_urls:
    
    
   # video = youtube.streams.get_highest_resolution()
    try:
        youtube=pytube.YouTube(link)
        print ( youtube.title," video time =>",sec2hm(youtube.length) ,"rating => ",round(youtube.rating,1) ,"views =>",views(youtube.views))
    except pytube.exceptions.VideoPrivate :
               
        print ("VideoPrivate")
        
    totaltime+=youtube.length
    totalviews+=youtube.views
print ("total time of PlayList hh:mm:ss ", sec2hm(totaltime) ,"Totalviews ",views(totalviews))    
#video.download()
