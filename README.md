# Stroke Predictor Application

A full-stack web application that predicts stroke risk based on patient health data using machine learning.

## 🏗️ Architecture

- **Backend**: Python Flask API with scikit-learn ML model
- **Frontend**: React.js web application
- **Model**: Random Forest Classifier trained on healthcare stroke data

## 🚀 Quick Start

### Option 1: Use Startup Scripts (Recommended)

**For macOS/Linux:**
```bash
./start.sh
```

**For Windows:**
```batch
start.bat
```

### Option 2: Manual Setup

#### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python app.py
   ```
   The backend will run on http://localhost:5001

#### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   The frontend will run on http://localhost:3000

## 📋 Usage

1. Open your browser and go to http://localhost:3000
2. Fill in the patient information form:
   - **Gender**: Male, Female, or Other
   - **Age**: Patient's age in years
   - **Hypertension**: Yes/No (history of high blood pressure)
   - **Heart Disease**: Yes/No (history of heart disease)
   - **Ever Married**: Yes/No (marital status)
   - **Work Type**: Private, Self-employed, Government job, Children, Never worked
   - **Residence Type**: Urban or Rural
   - **Average Glucose Level**: Blood glucose level (mg/dL)
   - **BMI**: Body Mass Index
   - **Smoking Status**: Never smoked, Formerly smoked, Smokes, Unknown

3. Click "Predict" to get the stroke risk assessment
4. View the prediction result with confidence score

## 🔧 API Endpoints

### POST /predict
Predicts stroke risk based on patient data.

**Request Body:**
```json
{
  "gender": "Male",
  "age": 45,
  "hypertension": 0,
  "heart_disease": 0,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Urban",
  "avg_glucose_level": 95.12,
  "bmi": 24.5,
  "smoking_status": "never smoked"
}
```

**Response:**
```json
{
  "stroke_prediction": 0,
  "confidence": 0.85,
  "message": "Low stroke risk"
}
```

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Features**: Age, BMI, glucose level, gender, hypertension, heart disease, marital status, work type, residence type, smoking status
- **Preprocessing**: 
  - Numerical features: Median imputation + Yeo-Johnson power transformation
  - Categorical features: One-hot encoding
- **Training Data**: Healthcare dataset with stroke occurrence records

## 📁 Project Structure

```
strokepredictor-/
├── backend/
│   ├── app.py              # Flask API server
│   ├── stroke_pred.py      # ML model utilities
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── App.css        # Styling
│   │   └── index.js       # React entry point
│   ├── public/
│   │   └── index.html     # HTML template
│   └── package.json       # Node.js dependencies
├── healthcare-dataset-stroke-data.csv  # Training data
├── start.sh               # Unix startup script
├── start.bat             # Windows startup script
└── README.md             # This file
```

## 🛠️ Development

### Backend Development
- The Flask server runs in debug mode with auto-reload
- CORS is enabled for frontend communication
- Comprehensive error handling and input validation

### Frontend Development
- React development server with hot-reload
- Form validation and user-friendly error messages
- Responsive design with clean UI

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: Make sure ports 3000 and 5001 are not being used by other applications
2. **Python dependencies**: Ensure you have Python 3.7+ installed
3. **Node.js dependencies**: Ensure you have Node.js 14+ and npm installed
4. **CORS issues**: The backend includes CORS headers, but ensure both servers are running

### Error Messages

- **"Could not get prediction"**: Backend server is not running or not accessible
- **"Invalid value for [field]"**: Input validation failed, check data format
- **Backend server startup fails**: Check if required Python packages are installed

## 📈 Model Performance

The Random Forest model provides:
- Binary classification (stroke/no stroke)
- Confidence scores for predictions
- Handles missing values and mixed data types
- Trained on balanced healthcare dataset

## 🔒 Security Notes

- This is a demonstration application
- Input validation is implemented but should be enhanced for production
- No patient data is stored - predictions are stateless
- Use HTTPS in production environment

## 📝 License

This project is for educational and demonstration purposes.