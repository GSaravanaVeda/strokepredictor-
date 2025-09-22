# Flask backend API for stroke prediction
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import PowerTransformer, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load and preprocess data (for demonstration, model is trained on startup)
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'healthcare-dataset-stroke-data.csv'))
df = pd.read_csv(csv_path)
df = df.drop('id', axis=1)

numerical = ['avg_glucose_level', 'bmi', 'age']
categorical = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

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

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Stroke Prediction API is running!',
        'version': '1.0.0',
        'endpoints': {
            'predict': 'POST /predict - Make stroke prediction'
        }
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'stroke-predictor'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Convert numeric strings to proper numbers
        numeric_fields = ['age', 'avg_glucose_level', 'bmi']
        for field in numeric_fields:
            if field in data and isinstance(data[field], str):
                try:
                    data[field] = float(data[field])
                except ValueError:
                    return jsonify({'error': f'Invalid value for {field}'}), 400
        
        # Convert categorical numeric strings to integers
        categorical_numeric_fields = ['hypertension', 'heart_disease']
        for field in categorical_numeric_fields:
            if field in data and isinstance(data[field], str):
                try:
                    data[field] = int(data[field])
                except ValueError:
                    return jsonify({'error': f'Invalid value for {field}'}), 400
        
        input_df = pd.DataFrame([data])
        pred = pipeline.predict(input_df)[0]
        prob = pipeline.predict_proba(input_df)[0][pred]
        
        return jsonify({
            'stroke_prediction': int(pred), 
            'confidence': round(float(prob), 3),
            'message': 'High stroke risk' if pred == 1 else 'Low stroke risk'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
	app.run(debug=True, port=5001)
