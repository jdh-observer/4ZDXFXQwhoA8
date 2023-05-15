FROM python:3.7
# config
RUN mkdir -p /var/www \
    && apt-get update \
    && apt-get install -y \
        build-essential \
        python-dev \
        git \
        python3-pip \
    && pip3 install -U pip

ENV SPACY_VERSION    2.3.2

# spacy
RUN \
    pip3 install -U catalogue \
        gensim \
        image \
        matplotlib \
        multiprocess \
        networkx \
        nltk \
        numpy \
        pandas \
        pdf2image \
        Pillow \
        pytesseract \
        requests \
        spacy \
        tomotopy \
        tqdm \
    && pip3 install -U spacy==${SPACY_VERSION} \
    && python3 -m spacy download en_core_web_sm



