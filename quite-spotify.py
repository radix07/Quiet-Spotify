from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import spotilib
import time

#pip install https://github.com/AndreMiras/pycaw/archive/master.zip

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
mute = volume.GetMute()
master = volume.GetMasterVolumeLevel()
volume.GetVolumeRange()

print("MasterVolumeLevel: %s" % volume.GetMasterVolumeLevel())

def mute():
    volume.SetMasterVolumeLevel(-60, None)
def unmute():
    global master
    volume.SetMasterVolumeLevel(master, None)
lastsong = ""
state = "unmute"
for i in range(0,1000):
    artist = spotilib.artist()
    song =   spotilib.song() 

    if lastsong != song:
        print artist,":",song

    if "There is noting" in artist or "There is noting" in song: 
        if state == "unmute":
            print "mute"
        mute()
        state = "mute"
    else:
        if state == "mute":
            print "unmute"
        else:
            master = volume.GetMasterVolumeLevel()
        unmute()
        state = "unmute"
    time.sleep(2)
    lastsong = song


