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

### convert only file data/test.srt to audio using autralian accent, a little bit faster, and save it to a different filename

```
docker run -v $(pwd)/data:/data -it tts --srt-file test.srt --lang en-au --tempo 1.35 --outfilename test-au

```

## Choosing your languages

A subtitle file is read by default in english. To choose an other language, juste specify in the filename following `filename.[language key].srt` where `[language key]` can be `fr` (french), `en`, `es` (spanish), `zh-CN` (chinese), ... Complete list can be found [here](https://pypi.python.org/pypi/gTTS)

### Known limitations

 * It use python 2.7...

 * Text have to be written on a single line:
```srt
﻿1
00:00:48,520 --> 00:00:49,350
It will work

2
00:00:50,280 --> 00:00:52,270
It will
not work

3
00:00:53,040 --> 00:00:56,310
lorem ipsum
```
