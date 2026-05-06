# 🏡 DreamHome Analytics & Price Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![UI/UX](https://img.shields.io/badge/UI%2FUX-Design_Focused-8A2BE2?style=for-the-badge)

**DreamHome Analytics** is an interactive, end-to-end web application that bridges the gap between machine learning and user-centric design. It analyzes real estate market trends and provides an AI-powered property price estimator wrapped in a clean, intuitive, and highly accessible user interface.

This project was built to demonstrate how complex data models can be translated into actionable, user-friendly digital experiences.

---

## ✨ Features

### 🎨 UI/UX Design Highlights
* **Clean, Minimalist Interface:** Built with custom CSS injections to ensure high readability, clear typography, and an uncluttered layout.
* **Intuitive Navigation:** Utilizes a tabbed layout to separate "Market Insights" from the "Price Predictor", preventing cognitive overload.
* **Interactive Visualizations:** Uses Plotly to create responsive, dynamic charts that allow users to explore data visually without feeling overwhelmed.
* **Clear Call-to-Actions (CTAs):** Strong visual hierarchy guiding the user effortlessly from inputting data to generating a prediction.

### 📊 Data Science & Backend Highlights
* **Automated Data Generation:** Includes a custom script to generate realistic, randomized real estate datasets based on logical market parameters.
* **Machine Learning:** Utilizes a **Random Forest Regressor** (`scikit-learn`) to predict housing prices based on features like square footage, age, and location score.
* **Data Processing:** Handles feature engineering and data splitting using `pandas` and `numpy`.

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit, Custom CSS, HTML
* **Data Visualization:** Plotly Express
* **Machine Learning:** Scikit-Learn
* **Data Manipulation:** Pandas, NumPy
* **Model Serialization:** Joblib

---

## 🚀 How to Run Locally

Follow these steps to get the project up and running on your local machine:

### 1. Clone the repository
```bash
git clone [https://github.com/Chinmayeeavancha/dreamhome-analytics.git](https://github.com/Chinmayeeavancha/dreamhome-analytics.git)
cd dreamhome-analytics
```

### 2. Install Dependencies
Make sure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Generate the Dataset
Run the data generator to create the `real_estate_data.csv` file:
```bash
python generate_data.py
```

### 4. Train the Machine Learning Model
Train the Random Forest model and save it as a `.pkl` file:
```bash
python train_model.py
```

### 5. Launch the Web App
Start the Streamlit UI dashboard:
```bash
streamlit run app.py
```
*The app will automatically open in your default web browser at `http://localhost:8501`.*

---

## 📁 Project Structure
```text
dreamhome_analytics/
│
├── requirements.txt       # Python dependencies
├── generate_data.py       # Script to generate realistic mock real estate data
├── train_model.py         # Script to train and save the Random Forest model
├── app.py                 # Main Streamlit application (Frontend/UI)
├── real_estate_data.csv   # Generated dataset (created after step 3)
└── house_price_model.pkl  # Serialized ML model (created after step 4)
```

---

## 💡 Future Roadmap
- [ ] Connect to a live real estate API (like Zillow or Redfin) for real-time data.
- [ ] Add a "Dark Mode" toggle for better accessibility.
- [ ] Implement advanced EDA profiling (e.g., correlation heatmaps).
- [ ] Expand prediction inputs to include neighborhood safety scores and school district ratings.

---

## 👩‍💻 Author

**Chinmayee Avancha**  
* Undergraduate Computer Science Engineering Student  
* Aspiring UI/UX Designer & Data Analyst  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/chinmayee-avancha)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Chinmayeeavancha)
