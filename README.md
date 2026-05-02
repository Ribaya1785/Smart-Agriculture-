# Smart-Agriculture-


# 🌾 Smart Agriculture Crop Recommendation System

A Machine Learning-based web application that recommends the best crop to grow based on soil and environmental conditions, along with profit estimation.

---

## 🚀 Features

* 🌱 Predicts the most suitable crop using ML model
* 📊 Shows **Top 3 crop recommendations** with confidence
* 💰 Calculates:

  * Market price
  * Expected yield
  * Gross revenue
  * Cultivation cost
  * Net profit per acre
  * ROI (Return on Investment)
* 🌐 User-friendly web interface using Flask

---

## 🧠 Technologies Used

* Python
* Flask (Web Framework)
* Scikit-learn (Machine Learning)
* NumPy
* HTML + CSS

---

## 📁 Project Structure

```
smart_agriculture/
│
├── app.py
├── crop_app.py
├── predict.py
├── model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── requirements.txt
│
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/smart-agriculture.git
cd smart-agriculture
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
python app.py
```

4. Open browser:

```
http://127.0.0.1:5000
```

---

## 📊 Input Parameters

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature (°C)
* Humidity (%)
* Soil pH
* Rainfall (mm)

---

## 📈 Output

* Recommended Crop
* Confidence Score
* Estimated Profit per Acre

---

## 🌍 Deployment

This project can be deployed using platforms like:

* Render
* Railway
* Heroku

---

## 🔮 Future Improvements

* Add real-time weather API
* Add fertilizer recommendation
* Improve UI with charts and graphs
* Mobile-friendly design

---

## 👨‍💻 Author

**Nihmath Ribaya**
Computer Science Engineering Student (AI/ML)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
