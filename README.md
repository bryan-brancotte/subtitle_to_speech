# subtitle_to_speech
convert subtitle (.srt) to speech (.wav) using google API

```
docker build . -t tts
```

```
docker run -v $(pwd)/data:/data -it tts
```
