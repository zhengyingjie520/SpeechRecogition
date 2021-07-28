#mport sys
#sys.path.append('/home/share/lmcproject/Task_one/autosub/')
#sys.path.append('/home/share/lmcproject/Task_one/autosub/baidusub3')
import main as autosub
videopath = 'i3.mp4'


if __name__ == '__main__':
    result = autosub.start(videopath=videopath)
    print(result)

