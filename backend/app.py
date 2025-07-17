from flask import Flask, jsonify #jsonify - helps send data (dictionaries/lists) nacl tp the browser as JSON. React will consume these responses later

from flask_cors import CORS #CORS - Lets your flask API accept requests from React frontend(which will run on a different port). Without this, your browser will block cross-origin requests
#for security

from recommender.preprocessing import load_data
from recommender.model import train_model, get_recommendations

app = Flask(__name__) #Creates a Flask app instance, __name__ tells flask to figure out where to find resources(like static files or templates) relative to this file

CORS(app) #Activate CORS protection for your app so React (local host:3000) can call your Flask API (local host:5000)

data_path = 'data/products.csv'
df = load_data(data_path)
train_model(df)

@app.route('/') #tells flask if someone runs the url using '/' it goes to the home function
def home():
    return jsonify({"message":"Hello from Flask API"})


@app.route('/recommend/<string:product>', methods=['GET'])
def recommend(product):
    recommendations = get_recommendations(product)
    return jsonify({"recommendations":recommendations})


if __name__ == '__main__': #Make sure Flask runs only if you execute app.py directly
    app.run(debug= True ) #Automatic server reload when you change the code
                        #Helpful error pages if something crashes

