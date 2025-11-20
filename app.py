from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))
model = pickle.load(open('final_model.pkl', 'rb'))
kmeans_rest = pickle.load(open('kmeans_restaurants.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    city = request.form['city']
    cuisine_type = request.form['cuisine']
    price = int(request.form['price_range'])
    checkins = int(request.form['checkin_count'])
    density = int(request.form['cluster_density'])

    input_data = pd.DataFrame({
        'latitude': [0],        # FIXME: dummy
        'longitude': [0],       # FIXME: dummy
        'price_range': [price],
        'checkin_count': [checkins],
        'cluster_density': [density],
        'cuisine': [cuisine_type],
        'city': [city]
    })

    X = preprocessor.transform(input_data)
    predicted_score = round(float(model.predict(X)[0]), 1)
    cluster = int(kmeans_rest.predict(X)[0])

    return render_template('result.html', score=predicted_score, cluster=cluster, city=city.title(), cuisine=cuisine_type.title())

if __name__ == '__main__':
    app.run(debug=True)