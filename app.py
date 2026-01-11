from flask import Flask, render_template, request, jsonify
from threading import Lock

app = Flask(__name__)

# ---------------- LIVE VIEWERS ----------------
live_viewers = 0
lock = Lock()  # thread-safe counter

# ---------------- HOME PAGE ----------------
@app.route('/')
def home():
    global live_viewers
    with lock:
        live_viewers += 1
    return render_template('index.html', viewers=live_viewers)

@app.route('/get_viewers')
def get_viewers():
    global live_viewers
    return jsonify({'viewers': live_viewers})

# ---------------- DISEASE PAGES ----------------
@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/liver')
def liver():
    return render_template('liver.html')

@app.route('/kidney')
def kidney():
    return render_template('kidney.html')

# ---------------- PREDICTION ROUTES ----------------
# ML will be added later – for now display inputs

@app.route('/predict-diabetes', methods=['POST'])
def predict_diabetes():
    pregnancies = request.form['pregnancies']
    glucose = request.form['glucose']
    bp = request.form['bp']
    bmi = request.form['bmi']

    return f"""
    <h2>Diabetes Prediction Input Received</h2>
    <p>Pregnancies: {pregnancies}</p>
    <p>Glucose Level: {glucose}</p>
    <p>Blood Pressure: {bp}</p>
    <p>BMI: {bmi}</p>
    <br>
    <a href="/">Back to Home</a>
    """

@app.route('/predict-heart', methods=['POST'])
def predict_heart():
    age = request.form['age']
    cholesterol = request.form['cholesterol']
    bp = request.form['bp']

    return f"""
    <h2>Heart Disease Input Received</h2>
    <p>Age: {age}</p>
    <p>Cholesterol: {cholesterol}</p>
    <p>Blood Pressure: {bp}</p>
    <br>
    <a href="/">Back to Home</a>
    """

@app.route('/predict-liver', methods=['POST'])
def predict_liver():
    bilirubin = request.form['bilirubin']
    alkaline = request.form['alkaline']
    proteins = request.form['proteins']

    return f"""
    <h2>Liver Disease Input Received</h2>
    <p>Total Bilirubin: {bilirubin}</p>
    <p>Alkaline Phosphatase: {alkaline}</p>
    <p>Total Proteins: {proteins}</p>
    <br>
    <a href="/">Back to Home</a>
    """

@app.route('/predict-kidney', methods=['POST'])
def predict_kidney():
    bp = request.form['bp']
    creatinine = request.form['creatinine']
    hemoglobin = request.form['hemoglobin']

    return f"""
    <h2>Kidney Disease Input Received</h2>
    <p>Blood Pressure: {bp}</p>
    <p>Serum Creatinine: {creatinine}</p>
    <p>Hemoglobin: {hemoglobin}</p>
    <br>
    <a href="/">Back to Home</a>
    """

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("Starting Cure++ Flask server...")
    app.run(debug=True)
