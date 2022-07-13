# mp3 to wav by pydub

import sys
import os
from pathlib import Path
from pydub import AudioSegment
import pdb

src = sys.argv[1]
src = Path(src)
try:
    dst = sys.argv[2] 
    dst = Path(dst)
except:
    dst = Path(src.parent)
    dst = dst/(src.stem + ".wav")

sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")