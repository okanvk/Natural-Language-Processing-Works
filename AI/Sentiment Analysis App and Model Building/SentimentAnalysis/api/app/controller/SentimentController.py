from flask import Blueprint, request
from flask import render_template
from app.services.ClassifierService import ClassifierService

sentiment_app = Blueprint('sentiment_app', __name__)

classifier_service = ClassifierService()

@sentiment_app.route('/main', methods=['POST','GET'])
def check_sentiment():
    try:
        if request.method == "GET":
            return render_template("index.html", result=-1)
        else:
            text = request.form['text']
            result = classifier_service.classify_text(text)
            print(result)
            return render_template("index.html", result=int(result))
    except:
        return render_template("index.html", result=-1)


