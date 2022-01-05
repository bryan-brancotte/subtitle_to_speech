#!/usr/bin/python
from gtts import gTTS
from subprocess import call
import os
import scriptine
import random
import string


def convert_string_to_wav(text, outfile_path, lang='en', delay=0, tempo=1.2):
    """
    Convert text into a wav file

    Args:
        :param text: the text to speech in latin encoding if wanter
        :param outfile_path: where to write the outfile
        :param lang: the language, english by default
        :param delay: in seconds
        :param tempo: speed of speech, google defaut is 1 but too slow

    """
    tts = gTTS(text=text.decode('utf-8'), lang=lang, slow=False).save(outfile_path+'.tmp.mp3')
    call(["mpg123", "-w", outfile_path+'.tmp.wav', outfile_path+'.tmp.mp3'])
    call(["sox", outfile_path+'.tmp.wav', outfile_path, "tempo", str(tempo), "delay", str(delay)])
    os.remove(outfile_path+'.tmp.wav')
    os.remove(outfile_path+'.tmp.mp3')
    
def convert_str_to_wav_in_docker_command(srt_file="", outfilename="", lang='', tempo=1.2):
    """
    Convert a subtitle file found in /data into a wav file

    Args:
        :param srt_file: filename of the subtitle file in srt format
        :param outfilename: filename of the outfile
        :param lang: the language, english by default
        :param tempo: speed of speech, google defaut is 1 but too slow

    """
    if srt_file == "":
        filenames = os.listdir('/data/')
    else:
        filenames = [srt_file, ]
    for file_name in filenames:
        if file_name[-4:] == ".srt":
            print ("language of %s: %s" % (file_name, lang))
            convert_str_to_wav_command(
                srt_file="/data/%s" % file_name,
                outfile_path="/data/%s.wav" % (file_name[:-4] if outfilename == "" else outfilename),
                lang=get_language_from_filename(file_name) if lang == "" else lang,
                tempo=tempo,
            )
    
def get_language_from_filename(file_name):
    try:
        rindex = file_name[:-4].rindex('.')+1
        if rindex == 0:
            raise Exception()
        return file_name[rindex:-4]
    except Exception:
        print("No language found. To specify it, ends the filename with .fr.srt or .en.srt") 
        return "en"

def convert_str_to_wav_command(srt_file, outfile_path, lang='en', tempo=-1):
    """
    Convert a subtitle file into a wav file

    Args:
        :param srt_file: path to the subtitle file in srt format
        :param outfile_path: where to write the outfile
        :param lang: the language, english by default
        :param tempo: speed of speech, google defaut is 1 but too slow

    """
    if tempo == -1 :
        if lang == "fr" :
            tempo = 1.35
        else:
            tempo = 1.2
    f = open(srt_file, 'r')
    lines = f.readlines()
    line_id=0
    part_files=[]
    ran_str=lang+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    tmp_outfile_path="/tmp/%s-out.wav"%ran_str
    while line_id+2<len(lines):
        try:
            name = lines[line_id+0].replace("\r","")[:-1]
            timming = lines[line_id+1].replace("\r","")[:-1]
            text = lines[line_id+2].replace("\r","")[:-1]
            delay = ((int(timming[0:2]) * 60 + int(timming[3:5])) * 60 + int(timming[6:8]))
            part_files.append("/tmp/%s-%s.wav"%(ran_str,name))
            convert_string_to_wav(
                text=text,
                outfile_path=part_files[-1],
                lang=lang,
                delay=delay,
                tempo=tempo,
            )
            line_id+=4
        except Exception as e:
            print("Error at line " + str(line_id) + " in " + srt_file)
            raise e
        #if len(part_files) == 2:
        #    call(['sox', '-m'] + part_files + [tmp_outfile_path])
        #elif len(part_files) > 2:
        #    call(['sox', '-m'] + part_files[:-1] + [tmp_outfile_path] + [tmp_outfile_path+'-out.wav'])
        #    call(['mv', tmp_outfile_path+'-out.wav', tmp_outfile_path])
    call(['sox', '-m'] + part_files + [tmp_outfile_path, 'norm'])
    call(['mv', tmp_outfile_path, outfile_path])
    call(["sox", outfile_path, outfile_path[:-3]+'ogg'])
    call(['rm'] + part_files)
    
    
#convert subtitle (.srt) to speech (.wav) using google API
if __name__ == '__main__':
    scriptine.run()
