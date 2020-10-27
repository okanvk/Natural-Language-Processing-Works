from tensorflow.keras.models import load_model
from nltk.stem import PorterStemmer
from app.constants import CLASSIFIER_PATH
from nltk import word_tokenize
import string
import re
import numpy as np
from nltk.corpus import stopwords



class NlpService:

    def __init__(self):
        self.classifier = load_model(CLASSIFIER_PATH)
        self.stemmer = PorterStemmer()

    def stem_text(self, text):
        words = word_tokenize(text)
        new_text = []
        for word in words:
            stemmed_word = self.stemmer.stem(word)
            new_text.append(stemmed_word)
        return " ".join(new_text)

    def remove_punctuation_and_stopwords(self,text):

        text_no_punctuation = [ch for ch in text if ch not in string.punctuation]
        text_no_punctuation = "".join(text_no_punctuation).split()

        list = " ".join([x.lower() for x in text_no_punctuation if not x.isdigit()]).split()

        text_no_punctuation_no_stopwords = \
            [word.lower() for word in list if word not in stopwords.words('english')]

        review = " ".join(text_no_punctuation_no_stopwords)
        return re.sub('\s+', ' ', review)

    def classify(self,vector):
        return self.classifier.predict_classes(np.expand_dims(vector, axis=0))[0][0]



