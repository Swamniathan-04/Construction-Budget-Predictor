from flask import Flask, request, jsonify
import pandas as pd
from ml_model import ConstructionBudgetPredictor

app = Flask(__name__)
predictor = ConstructionBudgetPredictor()
predictor.load_model()

@app.route('/')
def home():
    return 'Construction Budget Predictor API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    required_fields = [
        'project_area_sqft', 'num_floors', 'construction_type', 'location_urban',
        'complexity_score', 'materials_quality', 'labor_cost_per_sqft',
        'permits_and_fees', 'site_preparation_cost', 'utilities_cost',
        'project_duration_months'
    ]
    # Validate input
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    # Prepare input as DataFrame
    df = pd.DataFrame([data])
    try:
        prediction = predictor.predict(df)
        return jsonify({'predicted_budget': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 