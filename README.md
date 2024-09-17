# Confidence Classifier

This project aims to classify an person's confidence based on facial expressions captured from an image or webcam feed. It uses **DeepFace** to analyze emotions and map them to a confidence level.

## Files in the Repository

- **`app.py`**: The backend of the application, built using Flask, which processes the uploaded images, analyzes the facial expressions using DeepFace, and returns the predicted confidence level.
- **`index.html`**: The frontend of the application, where users can either upload an image or use their webcam to send images to the Flask backend every 5 seconds. The results are displayed on the page.

## How It Works

1. **Frontend (HTML & JavaScript)**:

   - The HTML page (`index.html`) allows users to either upload an image or capture images using their device's webcam.
   - Every 5 seconds, the captured image from the webcam is sent to the Flask API.
   - The API processes the image and returns a result indicating the candidate's **emotion** and **confidence** level.
   - The result is displayed on the web page in real-time.

2. **Backend (Flask)**:
   - The `app.py` script hosts the Flask server and handles incoming POST requests.
   - When an image is sent from the frontend, it is processed and analyzed using DeepFace's facial expression model.
   - Based on the emotion detected by DeepFace, the script maps the emotion to a confidence level (e.g., "happy" or "neutral" indicates confidence, while "sad" or "fear" indicates lack of confidence).
   - The result (emotion and confidence level) is returned as a JSON response to the frontend.

## Installation and Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- DeepFace

### Clone the Repository

```bash
git clone https://github.com/Shriram-11/Confidence_Classifier.git
cd Confidence_Classifier
```

### Spin up a Virtual Environment (Optional)

```bash
python -m venv env
```
Activate the virtual environment:

- On Windows (Command Prompt):
   ```ps1
   env\Scripts\activate.bat
   ```
- On Windows (Powershell):
   ```ps1
   .\env\Scripts\Activate.ps1
   ```
- On MacOS/Linux:
   ```bash
   source env/bin/activate
   ```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask App

```bash
python app.py
```

This will start the Flask server, and you should be able to access the application at `http://127.0.0.1:5000/`.

### Access the Frontend

1. Open a browser and navigate to `http://127.0.0.1:5000/`.
2. You can either upload an image or allow the webcam to capture and send images every 5 seconds.
3. The system will display the detected emotion and a corresponding confidence level.

## Emotion-to-Confidence Mapping

The following table shows how emotions are mapped to confidence levels:

| **Emotion** | **Confidence Level** |
| ----------- | -------------------- |
| Happy       | Confident            |
| Neutral     | Confident            |
| Angry       | Context-dependent    |
| Sad         | Not Confident        |
| Fear        | Not Confident        |
| Surprise    | Not Confident        |
| Disgust     | Not Confident        |

## Technologies Used

- **Flask**: Web framework for the backend API.
- **DeepFace**: Used for emotion detection and analysis.
- **JavaScript**: For handling webcam input and sending image data to the backend.
- **HTML/CSS**: For the basic structure and styling of the frontend.

## How to Contribute

If you have ideas for improving this project, feel free to fork the repository and submit a pull request.
