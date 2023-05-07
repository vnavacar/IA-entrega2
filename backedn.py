from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

app = Flask(__name__,template_folder='templates')

# Load the classifier
with open("Python/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)


@app.route("/", methods=["POST"])
def predict():
    text = request.json["text"]
    # Preprocess the input text using the same method you used to train the classifier
    processed_text = preprocess(text)   
    prediction = classifier.predict(np.array([processed_text]))[0]
     # Convert the prediction to a genre 
    return jsonify({"response_text": prediction})

if __name__ == "__main__":
    app.run(debug=True)

def preprocess(text):
    # Preprocess the input text
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    vectorizador = CountVectorizer(stop_words="english")
    vectorizador.fit([text])

    return text
with open("Python/classifier.pkl", "rb") as f:
    classifier = pickle.load(f)


@app.route('/', methods=['GET', 'POST'])
def main():
    if app.request.method == 'GET':
        return(app.render_template('main.html'))
    if app.request.method == 'POST':
        text = request.json["text"]
    # Preprocess the input text using the same method you used to train the classifier
        processed_text = preprocess(text)   
        prediction = classifier.predict(np.array([processed_text]))[0]
     # Convert the prediction to a genre 
        return jsonify({"response_text": prediction})
    
def preprocess(text):
    # Preprocess the input text
    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    vectorizador = CountVectorizer(stop_words="english")
    vectorizador.fit([text])

    return text    
if __name__ == "__main__":
    app.run(debug=True)
                                 