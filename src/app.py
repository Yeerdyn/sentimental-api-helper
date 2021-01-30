import flask
from flask import request, jsonify
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextToxicModel
from dostoevsky.models import FastTextSocialNetworkModel
import json
import sys
import os

tokenizer = RegexTokenizer()
toxicModel = FastTextToxicModel(tokenizer=tokenizer)
socialModel = FastTextSocialNetworkModel(tokenizer=tokenizer)

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Sentiment analysis api for russian language</h1><p>Based on <a href='https://github.com/bureaucratic-labs/dostoevsky'>Dostoevsky</a>.</p>"


@app.route('/sentimental', methods=['GET'])
def sentimetal():
    try:
        if 'message' in request.args:
            message = request.args['message']

            messages = [message]
            toxicResult = toxicModel.predict(messages, k=2)[0]
            socialResult = socialModel.predict(messages, k=2)[0]

            results = {
                'toxic': toxicResult,
                'social': socialResult
            }

            return json.dumps(results, sort_keys=True, indent=4), 200
        else:
            return "Error: No message field provided. Please specify an message.", 400
    except Exception:
        return "Error: cannot operate with this message", 500
app.run(host='0.0.0.0', port=80)