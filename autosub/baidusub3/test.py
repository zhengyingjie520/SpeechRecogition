import main as autosub
import sys
sys.path.append("D:\下载\Autosub_Multiple_Methods")
from moviepy.editor import *
from merge import RealizeAddSubtitles
import moviepy.editor as mp
# 本地视频位置
from moviepy.video.VideoClip import TextClip

videopath = '../video/i3.mp4'
strV = "../video/i3.mp4"
strL = "../video/i3.jpg"
result = "D:\\下载\\Autosub_Multiple_Methods\\video\\out.mp4"
# 功能一：自动生成字幕功能
# 参数str1:表示输入视频的路径
# 参数str2:表示字幕生成的路径
def generateSub(videopath):
    result = autosub.start(videopath = videopath)
    return result

# 功能二：自动生成字幕功能
# 参数str1:表示输入视频的路径
# 参数str2:表示视频输出的路径
def merge(str1,srtpath,myfontsize,myfont,mycolor):
    print(myfont)
    str2=RealizeAddSubtitles(str1,srtpath,myfontsize,myfont,mycolor)
    return str2

# 功能三：提取背景声音
def GetAudio(inUrl,outUrl):
    video = VideoFileClip(inUrl)
    audio = video.audio
    audio.write_audiofile(outUrl)

# 功能四：去除视频中的水印logo
def movelogo(input,output,x,y,w,h):
    cmd = "cmd.exe /c ffmpeg -i " + input + " -filter_complex \"delogo=x=" + x + ":y=" + y + ":w=" + w + ":h=" + h + ":show=0\" " + output
    os.system(cmd)

# 中间方法，生成logo
def addlogoInVideo(v, l):
    # 视频
    video = mp.VideoFileClip(v)
    # 水印
    logo = (mp.ImageClip(l)
            .set_duration(video.duration)  # 水印持续时间
            .resize(height=100)  # 水印的高度，会等比缩放
            .margin(right=30, top=30, opacity=0)  # 水印边距和透明度
            .set_pos(("right", "top")))  # 水印的位置
    return video,logo

# 功能五：添加视频中的水印,output1
def func(v,l,result):
    output = mp.CompositeVideoClip(addlogoInVideo(v,l))
    output.write_videofile(result, audio_codec="aac")
    return result

# 测试1：自动生成字幕
# print(merge(videopath))
# 测试2：去除水印logo
# movelogo("E:\\Autosub_Multiple_Methods\\video\\1.mp4","E:\\Autosub_Multiple_Methods\\video\\out.mp4","1185","35","85","125")
# 测试3：添加水印logo
# print(func(strV,strL,result))
if __name__ == '__main__':
    parm = sys.argv
    print(parm)
    if parm[1] =='1':
        print(generateSub(parm[2]))
    elif parm[1] =='2':
        print(merge(parm[2],parm[3],int(parm[4]),parm[5],parm[6]))
    elif parm[1] =='3':
        GetAudio(parm[2],parm[2])
    elif parm[1] =='4':
        movelogo(parm[2],parm[3],parm[4],parm[5],parm[6],parm[7])
    else:
        print(func(parm[2],parm[3],parm[4]))