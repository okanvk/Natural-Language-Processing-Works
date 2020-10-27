from app.services.NLPService import NlpService
from app.services.Word2VecService import Word2VecService


class ClassifierService:

    def __init__(self):
        self.word2vec_service = Word2VecService()
        self.nlp_service = NlpService()


    def classify_text(self,text):

        clean_text = self.nlp_service.remove_punctuation_and_stopwords(text)

        clean_stemmed_text = self.nlp_service.stem_text(clean_text)

        vector = self.word2vec_service.prepare_embeddings(clean_stemmed_text)

        vector_shaped = vector.reshape(300,)

        output = self.nlp_service.classify(vector_shaped)

        return output

