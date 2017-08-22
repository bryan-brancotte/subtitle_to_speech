FROM python:2.7

RUN apt-get update && apt-get install -y \
		mpg123 \
		sox \
	&& rm -rf /var/lib/apt/lists/*	

ADD ./requirements.txt /

RUN pip install --upgrade pip \
    && pip install -r /requirements.txt

RUN mkdir /data && chmod 77 /data

ENTRYPOINT  ["python","/subtitle_to_speech.py", "convert-str-to-wav-in-docker"]
	
ADD ./subtitle_to_speech.py /
