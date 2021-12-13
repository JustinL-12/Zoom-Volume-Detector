import pycaw
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time

while (True):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if (session.Process and session.Process.name() == "Zoom.exe" and volume.GetMasterVolume() == 1):
            volume.SetMasterVolume(0.25, None)
    time.sleep(.5)
    