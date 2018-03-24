import numpy as np
import pandas as pd

# Install packages and libraries
# This only needs to be done once per notebook.


# installing nltk and its packages
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')


# Installing textract
!apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf \
poppler-utils libpulse-dev pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
!pip install textract


# Installing textblob
!pip install - U textblob
# from textblob import TextBlob


# Install the PyDrive wrapper & import libraries.
!pip install - U - q PyDrive
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from google.colab import auth
# from oauth2client.client import GoogleCredentials
