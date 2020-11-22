def getsec(vtime):

    h, m, s,ms = vtime.split(':')
 
    xtime=int(h) * 3600 + int(m) * 60 + int(s) +int(ms)*0.1
  

    return xtime


startime= getsec ('00:00:25:00')
endtime=getsec ('00:13:46:00')
print ("clip time: ",endtime-startime)
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("fra.mp4", startime, endtime, targetname="fraclip.mp4")
