from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the classifier
with open("classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

@app.route("/", methods=["POST"])
def predict():
    text = request.json["text"]
    # Preprocess the input text using the same method you used to train the classifier
    processed_text = preprocess(text)
    prediction = classifier.predict(np.array([processed_text]))[0]
    genre = label_to_genre(prediction) # Convert the prediction to a genre 
    return jsonify({"response_text": genre})

if __name__ == "__main__":
    app.run(debug=True)