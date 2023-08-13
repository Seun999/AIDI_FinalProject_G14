from flask import Flask, request, jsonify
from transformers import pipeline
import pygame

app = Flask(__name__)

# Load a language model for text classification
model = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.route('/predict', methods=['POST'])
def predict_instrument():
    data = request.json
    instrument_name = data.get('instrument_name', '')

    if instrument_name:
        result = model(instrument_name)[0]
        predicted_instrument = result['label']
        confidence = result['score']

        return jsonify({'instrument_name': predicted_instrument, 'confidence': confidence})
    else:
        return jsonify({'error': 'Instrument name is missing'})

if __name__ == "__main__":
    app.run(debug=True)
