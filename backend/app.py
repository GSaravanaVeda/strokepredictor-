# Flask backend API for stroke prediction
from flask import Flask, request, jsonify
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import PowerTransformer, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

app = Flask(__name__)

# Load and preprocess data (for demonstration, model is trained on startup)
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'healthcare-dataset-stroke-data.csv'))
df = pd.read_csv(csv_path)
df = df.drop('id', axis=1)

numerical = ['avg_glucose_level', 'bmi', 'age']
categorical = ['hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

transformer = ColumnTransformer(transformers=[
	('num', Pipeline(steps=[
		('imputer', SimpleImputer(strategy='median')),
		('power', PowerTransformer(method='yeo-johnson', standardize=True))
	]), numerical),
	('cat', OneHotEncoder(), categorical)
])

X = df.drop('stroke', axis=1)
y = df['stroke']

pipeline = Pipeline([
	('transformer', transformer),
	('model', RandomForestClassifier(n_estimators=100))
])
pipeline.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
	data = request.get_json()
	input_df = pd.DataFrame([data])
	pred = pipeline.predict(input_df)[0]
	prob = pipeline.predict_proba(input_df)[0][pred]
	return jsonify({'stroke_prediction': int(pred), 'confidence': round(prob, 3)})

if __name__ == '__main__':
	app.run(debug=True, port=5001)
