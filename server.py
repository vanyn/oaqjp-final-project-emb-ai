"""final lab to detect emotion from inputted string"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """calls the emotion detection tool and returns results"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return f"For the given statement, the system response is \
    'anger': {response['anger']}, 'disgust': {response['disgust']}, \
    'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. \
    The dominant emotion is <strong>{dominant_emotion}</strong>."

@app.route("/")

def render_index_page():
    """root entry page"""
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
