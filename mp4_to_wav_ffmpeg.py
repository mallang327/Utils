# mp3 to wav by pydub

import sys
import os
from pathlib import Path
import pdb
import subprocess

src = sys.argv[1]
src = Path(src)
try:
    dst = sys.argv[2] 
    dst = Path(dst)
except:
    dst = Path(src.parent)
    dst = dst/(src.stem + ".wav")

command = "ffmpeg -i " + str(src) + " -ab 100k -ac 2 -ar 44100 -vn " + str(dst)

subprocess.call(command, shell=True)