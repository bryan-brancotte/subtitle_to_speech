# subtitle to speech
This tool help you to convert subtitle (.srt) to audio file (.wav and .ogg). As the tool is based on [Docker](https://www.docker.com/what-docker), it is OS independant :)

It uses Google text to speech API, mpg123 and sox

```
docker build . -t tts
```

```
docker run -v $(pwd)/data:/data -it tts
```
