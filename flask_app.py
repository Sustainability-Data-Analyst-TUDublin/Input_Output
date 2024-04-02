from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from flask import Flask, request, jsonify
from torch.nn.functional import softmax

app = Flask(__name__)

# Adjust these paths if necessary
model_path = "./final_saved_model_multi"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

@app.route('/')
def home():
    return "Model loaded and ready to analyze text!"

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    text = data['text']
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = softmax(logits, dim=1).tolist()

    # Assuming you want to return the probabilities
    return jsonify(probabilities)
