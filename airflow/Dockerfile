FROM apache/airflow

#USER root
#
#RUN apt-get update && \
#    apt-get -y install gcc && apt-get -y install g++ && apt-get -y install python-dev && \
#        apt-get -y install python3-dev && apt-get -y install libevent-dev

#USER airflow

RUN pip install --user -U pip setuptools

COPY requirements.txt /opt/

WORKDIR /opt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt

RUN python -m nltk.downloader vader_lexicon

RUN python -m spacy download en_core_web_md

#RUN python -c 'from summarizer import Summarizer; model = Summarizer()'

#torch
#bert-extractive-summarizer
#transformers

USER root
RUN chmod 755 /opt/

USER airflow