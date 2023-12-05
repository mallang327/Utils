# Utils

**Utils_for_everything**

****
* mp3_to_wav_pydub.py [audio 파일 형식 변환]

pydub 라이브러리 사용하여 mp3 파일을 wav 파일로 변환

저장 경로 없을 경우 불러온 파일이 있는 곳에 같은 이름으로 저장

```
python mp3_to_wav_pydub.py [file_location] [save_location/file_name.wav]
```
****
* mp4_to_wav_ffmpeg.py [audio 추출]

subprocess 이용하여 linux ffmpeg 어플리케이션 사용

저장 경로 없을 경우 불러온 파일이 있는 곳에 같은 이름으로 저장

```
python mp4_to_wav_ffmpeg.py [file_location] [save_location/file_name.wav]
```
****
* crawling_mostreplayed.py [많이 다시 본 장면 추출 from Youtube]

YouTube operational API 사용해서 most replayed start time과 duration 추출

youtube-dl 사용해서 audio file download

[(Github Link) YouTube-operational-API](https://github.com/Benjamin-Loison/YouTube-operational-API)

[(Github Link) Youtube-dl](https://github.com/ytdl-org/youtube-dl)

****
* pytorch_to_cpp.py [torch script로 변환]

torch.jit.script를 통해 torch script로 변환해서 cpp 환경에서 사용할 수 있는 모델 형태로 변환

