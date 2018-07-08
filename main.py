import time
import os

bpm = 151

if 40 < bpm < 180:
    os.system("/home/pi/Desktop/Scripts/{}.sh".format(bpm))
    
else:
     
