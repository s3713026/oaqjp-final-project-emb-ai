"""
Flask server for Emotion Detection application.
Provides a web interface and API endpoint to analyze emotions in text.
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the homepage with the user input form.
    
    Returns:
        str: Rendered HTML template for index page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    API endpoint to detect emotions in a given text.
    Uses emotion_detector function and handles blank input gracefully.
    
    Query Parameters:
        text (str): The input text to analyze.
    
    Returns:
        dict: JSON response containing emotions and dominant emotion,
              or error message if input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
