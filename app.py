# import necessary libraries
from flask import Flask, url_for, render_template
from forms import InputForm
import pandas as pd
import joblib

# initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

#load the trained model
model = joblib.load('model.joblib')

# Define the route for the home page and prediction page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Create an instance of the InputForm
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame(dict(
            airline=[form.airline.data],
            date_of_journey=[form.date_of_journey.data.strftime('%Y-%m-%d')],
            source=[form.source.data],
            destination=[form.destination.data],
            dep_time=[form.dep_time.data.strftime('%H:%M:%S')],
            arrival_time=[form.arrival_time.data.strftime('%H:%M:%S')],
            duration=[form.duration.data],
            total_stops=[form.total_stops.data],
            additional_info=[form.additional_info.data]
        ))
        prediction = model.predict(x_new)[0]
        message = f"The predicted price is {prediction:,.0f} INR"
    else:
        message = "Kindly ❤️ fill out the form to get a prediction."
    return render_template('predict.html', title='Predict', form=form, output=message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)