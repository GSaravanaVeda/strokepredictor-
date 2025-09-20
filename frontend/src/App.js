import React, { useState } from 'react';
import './App.css';

function App() {
  const [form, setForm] = useState({
    gender: '',
    age: '',
    hypertension: '',
    heart_disease: '',
    ever_married: '',
    work_type: '',
    Residence_type: '',
    avg_glucose_level: '',
    bmi: '',
    smoking_status: ''
  });
  const [result, setResult] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setConfidence(null);
    try {
  const response = await fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });
      const data = await response.json();
      setResult(data.stroke_prediction);
      setConfidence(data.confidence);
    } catch (error) {
      setResult('Error: Could not get prediction');
      setConfidence(null);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h2>Stroke Prediction</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label className="form-label">gender:</label>
          <select className="form-input" name="gender" value={form.gender} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
        </div>
        <div>
          <label className="form-label">age:</label>
          <input className="form-input" type="number" name="age" value={form.age} onChange={handleChange} required />
        </div>
        <div>
          <label className="form-label">hypertension:</label>
          <select className="form-input" name="hypertension" value={form.hypertension} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="0">No</option>
            <option value="1">Yes</option>
          </select>
        </div>
        <div>
          <label className="form-label">heart_disease:</label>
          <select className="form-input" name="heart_disease" value={form.heart_disease} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="0">No</option>
            <option value="1">Yes</option>
          </select>
        </div>
        <div>
          <label className="form-label">ever_married:</label>
          <select className="form-input" name="ever_married" value={form.ever_married} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>
        </div>
        <div>
          <label className="form-label">work_type:</label>
          <select className="form-input" name="work_type" value={form.work_type} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="Private">Private</option>
            <option value="Self-employed">Self-employed</option>
            <option value="Govt_job">Govt_job</option>
            <option value="children">children</option>
            <option value="Never_worked">Never_worked</option>
          </select>
        </div>
        <div>
          <label className="form-label">Residence_type:</label>
          <select className="form-input" name="Residence_type" value={form.Residence_type} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="Urban">Urban</option>
            <option value="Rural">Rural</option>
          </select>
        </div>
        <div>
          <label className="form-label">avg_glucose_level:</label>
          <input className="form-input" type="number" name="avg_glucose_level" value={form.avg_glucose_level} onChange={handleChange} required />
        </div>
        <div>
          <label className="form-label">bmi:</label>
          <input className="form-input" type="number" name="bmi" value={form.bmi} onChange={handleChange} required />
        </div>
        <div>
          <label className="form-label">smoking_status:</label>
          <select className="form-input" name="smoking_status" value={form.smoking_status} onChange={handleChange} required>
            <option value="">Select</option>
            <option value="formerly smoked">formerly smoked</option>
            <option value="never smoked">never smoked</option>
            <option value="smokes">smokes</option>
            <option value="Unknown">Unknown</option>
          </select>
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Predicting...' : 'Predict'}
        </button>
      </form>
      {result !== null && (
        <div className="result">
          <strong>Prediction:</strong> {result === 1 ? 'Stroke Risk' : result === 0 ? 'No Stroke Risk' : result}
          {confidence !== null && (
            <div><strong>Confidence:</strong> {confidence}</div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
