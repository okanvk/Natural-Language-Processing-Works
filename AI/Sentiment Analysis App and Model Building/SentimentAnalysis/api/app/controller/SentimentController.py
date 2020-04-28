from flask import Blueprint, request, jsonify, abort

from app.services.ClassifierService import ClassifierService

sentiment_app = Blueprint('sentiment_app', __name__)

classifier_service = ClassifierService()

@sentiment_app.route('/check_sentiment', methods=['POST'])
def check_sentiment():

    text = request.json['text']

    result = classifier_service.classify_text(text)

    return jsonify({"result" : int(result)})

