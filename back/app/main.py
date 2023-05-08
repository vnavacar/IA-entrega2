
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

#with open("classifier.pkl", "rb") as f:
 #   classifier = pickle.load(f)



@app.route('/', methods=['POST'])
def prediction():
    classifier = pickle.load(open('classifier.pkl','rb'))
    text = request.get_json("text")
    # Preprocess the input text using the same method you used to train the classifier
    #processed_text = preprocess(text)
    prediction = classifier.predict([text["text"]])
    
     # Convert the prediction to a genre 
    if prediction == 0:
        return jsonify({"categoria": "Comedia"})
    if prediction == 1:
        return jsonify({"categoria": "Horror"})
    

	
