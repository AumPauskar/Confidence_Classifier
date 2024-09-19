from flask import Flask, request, jsonify
import base64
from io import BytesIO
from PIL import Image
from deepface import DeepFace
import numpy as np
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Mapping of emotions to confidence levels
CONFIDENCE_MAP = {
    'happy': 'Confident',
    'neutral': 'Confident',
    'surprise': 'Not Confident',
    'sad': 'Not Confident',
    'fear': 'Not Confident',
    'angry': 'Not Confident',
    'disgust': 'Not Confident'
}

# Function to decode base64 image and convert it to PIL Image
def decode_base64_image(base64_str):
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))
    return image

# Function to predict emotion using DeepFace
def predict_confidence(image):
    try:
        # Convert the image to a format compatible with DeepFace
        image = np.array(image)

        # Use DeepFace to analyze emotions
        analysis = DeepFace.analyze(image, actions=['emotion'])

        # Print analysis to debug its structure
        app.logger.debug(f"DeepFace analysis result: {analysis}")

        # If 'emotion' is a dictionary inside a list
        if isinstance(analysis, list):
            dominant_emotion = analysis[0]['dominant_emotion']
        else:
            dominant_emotion = analysis['dominant_emotion']

        # Map the emotion to confidence level
        confidence = CONFIDENCE_MAP.get(dominant_emotion, "Not Confident")
        return confidence, dominant_emotion

    except Exception as e:
        app.logger.error(f"Error analyzing image: {e}")
        raise

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Check if 'image' is in the request JSON
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    base64_image = data['image']

    try:
        # Decode the base64 image
        image = decode_base64_image(base64_image)

        # Predict confidence level based on emotion
        confidence, emotion = predict_confidence(image)

        # Return the result
        return jsonify({
            'confidence': confidence,
            'emotion': emotion
        })

    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': f'Failed to detect emotion: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')