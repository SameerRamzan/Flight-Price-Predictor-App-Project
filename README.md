# ✈️ Flight Price Prediction App
A web-based application built using Flask that predicts flight ticket prices based on user inputs like departure time, arrival time, source, destination, airline, and more. The prediction model is trained on a real-world Indian flights dataset.

## 🔍 Overview
This project demonstrates the end-to-end pipeline of a Machine Learning Web Application, including:

- Data preprocessing and model training.

- Building a Flask-based web server.

- Creating an interactive UI to gather user inputs.

- Serving model predictions to the frontend.

## 🚀 Demo
Try the application locally to see real-time flight price predictions based on your custom inputs!

## 🧠 Model Info
Algorithm Used: Random Forest Regressor

- Training Data: Cleaned Indian Flights dataset with features like:

- Airline

- Source

- Destination

- Total Stops

- Journey Date & Time

- Duration

- Price (target variable)

# 💻 Tech Stack
- **Backend**: Python, Flask

- **Machine Learning**: scikit-learn, pandas, numpy

- **Frontend**: HTML/CSS (Jinja2 templating)

- **Deployment**: Localhost (can be extended to cloud deployment)

## 🔧 How to Run Locally, Clone the Repository

bash

```
git clone https://github.com/SameerRamzan/Flask-Final-Project.git
cd Flask-Final-Project
```
### Install Dependencies

bash

```
pip install -r requirements.txt
```
Run the Flask App

bash
```
python app.py
```

## 📊 Sample Input & Output
**Input Example**:

**Airline**: IndiGo

**Source**: Delhi

**Destination**: Cochin

**Departure**: 10:00 AM

**Arrival**: 02:30 PM

**Total Stops**: 1

**Predicted Price**: ₹4,582 (example output)

## 📌 Future Enhancements
- Add data visualizations for feature analysis.

- Enable cloud deployment (Heroku / Render / AWS).

- Collect real-time flight data via API.

- Improve UI/UX with JavaScript and Bootstrap.

# 🙌 Acknowledgements
**Dataset**: Kaggle – Flight Price Prediction

**Framework**: Flask

**Author**: ***Muhammad Sameer***