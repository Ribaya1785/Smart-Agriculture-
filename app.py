from flask import Flask, render_template, request, jsonify
import pickle, numpy as np

app = Flask(__name__)

# Load model, scaler, encoder once at startup
with open('model.pkl', 'rb') as f: model = pickle.load(f)
with open('scaler.pkl', 'rb') as f: scaler = pickle.load(f)
with open('label_encoder.pkl', 'rb') as f: le = pickle.load(f)

# Same profit dict from Stage 6
CROP_PROFIT ={
    'rice': (20, 2500),
    'maize': (18, 2000),
    'coffee': (200, 500),
    'orange': (30, 5000),
    'banana': (25, 12000),
    'mango': (40, 4000),
    'grapes': (60, 6000)
}
# Route 1: Show the web page
@app.route('/')
def index():
    return render_template('index.html')

# Route 2: Handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get values from the form
    data = [
        float(request.form['N']),
        float(request.form['P']),
        float(request.form['K']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall']),
    ]
    arr = np.array([data])
    arr_scaled = scaler.transform(arr)
    pred = model.predict(arr_scaled)
    crop = le.inverse_transform(pred)[0]
    proba = model.predict_proba(arr_scaled)[0]
    top3_idx = np.argsort(proba)[::-1][:3]
    top3 = [(le.classes_[i],round(proba[i]*100,1)) for i in top3_idx]
    confidence = top3[0][1]
# Get profit info
    price, yld = CROP_PROFIT.get(crop, (30, 1000))
    profit = price * yld - 15000

    return render_template('index.html',
        crop=crop,
        confidence=confidence,
        profit=f"₹{profit:,}",
        top3=top3,
        price=price,
        yield_val=yld,
        revenue=f"{price*yld:,}",
        cost=15000,
        roi=round((profit/15000)*100,1)
    )

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=10000)
    # Open browser: http://127.0.0.1:5000
