* To record I used recordmydesktop (see script in PJ)
* As I was recording my browser and wanted it to be pixel-sized with 1920x1080 (rush in native HD) I used [window-resizer-beta](https://chrome.google.com/webstore/detail/window-resizer-beta/pnhnbekjlbamfnnemcaolkjchjlidbib?utm_source=chrome-app-launcher-info-dialog)
* Finally for editing I used kdenlive, with a rendering in mp4 H.264 / AAC High Profile. When I used it, it happens to crash, so do backup VERY often. Ergonomically, it looks like a final cut pro like.
* For subtitles I used Gaupol, but youtube tool is easier to use
* To add sound, I used [subtitle to speech](https://github.com/bryan-brancotte/subtitle_to_speech) ;)
* For hosting it's youtube
* An example (without audio at the time) is here https://www.youtube.com/watch?v=6bAM17724Zo, watch in HD if possible


```sh
#!/bin/sh

export WORK_DIR=/tmp/rec
mkdir -p $WORK_DIR

export DEST_DIR=~/Documents/video/rush
mkdir -p $DEST_DIR

recordmydesktop -o $DEST_DIR/take  --no-sound --fps=25 -x=1780 -y=100 --width=1920 --height=1080 --workdir=$WORK_DIR/
```
