# subtitle to speech

## What is it ?

This tool help you to convert subtitle (.srt) to audio file (.wav and .ogg). As the tool is based on [Docker](https://www.docker.com/what-docker), it is OS independant :)

It uses Google text to speech API, [mpg123](https://www.mpg123.de/) and [sox](http://sox.sourceforge.net/sox.html)

### build it

```
docker build . -t tts
```

### convert all srt files that we can find in ./data directory

```
docker run -v $(pwd)/data:/data -it tts
```

## Choosing your languages

A subtitle file is read by default in english. To choose an other language, juste specify in the filename following `filename.[language key].srt` where [language key] can be `fr` (french), `en`, `es` (spanish), `zh-CN` (chinese), ...
