from flask import Flask

def create_app() -> Flask:
    flask_app = Flask('sentiment_api')
    from app.controller.SentimentController import sentiment_app
    flask_app.register_blueprint(sentiment_app)
    return flask_app