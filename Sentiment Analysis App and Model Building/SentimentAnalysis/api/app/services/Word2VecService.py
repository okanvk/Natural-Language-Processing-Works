from app.models.Word2VecModel import Word2VecModel
import numpy as np

class Word2VecService:

        def __init__(self):
            self.word2vec = Word2VecModel()

        def prepare_embeddings(self, text):
            processed_data = self.word2vec.preprocess_label(text)
            vector = self.word2vec.getAvgFeatureVecs(processed_data)
            vector[np.isnan(vector)] = 0
            dataVects = np.asarray(vector)
            return dataVects





