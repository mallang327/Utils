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
