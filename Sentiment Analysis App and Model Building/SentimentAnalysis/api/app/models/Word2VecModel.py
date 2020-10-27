from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize
import numpy as np
from app.constants import WORD2_VEC_MODEL_PATH


class Word2VecModel:

    def __init__(self):
        self.model = Word2Vec.load(WORD2_VEC_MODEL_PATH)
        self.num_features = 300

    def preprocess_label(self,review_text):
        words = review_text.split()
        return (words)

    def labels_to_sentences(self,label):
        raw_sentences = sent_tokenize(label)
        sentences = []
        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0:
                sentences.append(self.preprocess_label(raw_sentence))
        return sentences

    def featureVecMethod(self,words, model):
        featureVec = np.zeros(self.num_features, dtype="float32")
        nwords = 0

        index2word_set = set(model.wv.index2word)

        for word in words:
            if word in index2word_set:
                nwords = nwords + 1
                featureVec = np.add(featureVec, model[word])

        featureVec = np.divide(featureVec, nwords)
        return featureVec

    def getAvgFeatureVecs(self, review):
        reviewFeatureVecs = np.zeros((1, self.num_features), dtype="float32")
        reviewFeatureVecs[0] = self.featureVecMethod(review, self.model)
        return reviewFeatureVecs


