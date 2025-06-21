import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

class ConstructionBudgetPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def generate_sample_data(self, n_samples=1000):
        """Generate sample construction project data for training"""
        np.random.seed(42)
        
        data = {
            'project_area_sqft': np.random.uniform(1000, 50000, n_samples),
            'num_floors': np.random.randint(1, 21, n_samples),
            'construction_type': np.random.choice(['residential', 'commercial', 'industrial'], n_samples),
            'location_urban': np.random.choice([0, 1], n_samples),
            'complexity_score': np.random.uniform(1, 10, n_samples),
            'materials_quality': np.random.choice(['low', 'medium', 'high'], n_samples),
            'labor_cost_per_sqft': np.random.uniform(50, 200, n_samples),
            'permits_and_fees': np.random.uniform(5000, 50000, n_samples),
            'site_preparation_cost': np.random.uniform(10000, 100000, n_samples),
            'utilities_cost': np.random.uniform(5000, 30000, n_samples),
            'project_duration_months': np.random.uniform(3, 24, n_samples)
        }
        
        df = pd.DataFrame(data)
        
        # Calculate target variable (total budget)
        base_cost = df['project_area_sqft'] * df['labor_cost_per_sqft']
        complexity_multiplier = 1 + (df['complexity_score'] - 5) * 0.1
        materials_multiplier = df['materials_quality'].map({'low': 0.8, 'medium': 1.0, 'high': 1.3})
        location_multiplier = 1 + df['location_urban'] * 0.2
        
        df['total_budget'] = (base_cost * complexity_multiplier * materials_multiplier * location_multiplier + 
                             df['permits_and_fees'] + df['site_preparation_cost'] + df['utilities_cost'])
        
        # Add some noise to make it more realistic
        df['total_budget'] += np.random.normal(0, df['total_budget'] * 0.1)
        
        return df
    
    def prepare_features(self, df):
        """Prepare features for the model"""
        # Convert categorical variables to numerical
        df_encoded = df.copy()
        df_encoded['construction_type'] = df_encoded['construction_type'].map({
            'residential': 0, 'commercial': 1, 'industrial': 2
        })
        df_encoded['materials_quality'] = df_encoded['materials_quality'].map({
            'low': 0, 'medium': 1, 'high': 2
        })
        
        # Select features for the model
        feature_columns = [
            'project_area_sqft', 'num_floors', 'construction_type', 'location_urban',
            'complexity_score', 'materials_quality', 'labor_cost_per_sqft',
            'permits_and_fees', 'site_preparation_cost', 'utilities_cost',
            'project_duration_months'
        ]
        
        X = df_encoded[feature_columns]
        y = df_encoded['total_budget']
        
        return X, y
    
    def train(self, X_train, y_train):
        """Train the model"""
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Train the model
        self.model.fit(X_train_scaled, y_train)
        self.is_trained = True
        
        print("Model trained successfully!")
    
    def predict(self, X):
        """Make predictions"""
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def evaluate(self, X_test, y_test):
        """Evaluate the model"""
        if not self.is_trained:
            raise ValueError("Model must be trained before evaluation")
        
        y_pred = self.predict(X_test)
        
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Performance:")
        print(f"Mean Absolute Error: ${mae:,.2f}")
        print(f"Root Mean Square Error: ${rmse:,.2f}")
        print(f"R² Score: {r2:.4f}")
        
        return {
            'mae': mae,
            'rmse': rmse,
            'r2': r2,
            'predictions': y_pred
        }
    
    def save_model(self, filepath='construction_budget_model.pkl'):
        """Save the trained model"""
        if not self.is_trained:
            raise ValueError("Model must be trained before saving")
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'feature_names': [
                'project_area_sqft', 'num_floors', 'construction_type', 'location_urban',
                'complexity_score', 'materials_quality', 'labor_cost_per_sqft',
                'permits_and_fees', 'site_preparation_cost', 'utilities_cost',
                'project_duration_months'
            ]
        }
        
        joblib.dump(model_data, filepath)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath='construction_budget_model.pkl'):
        """Load a trained model"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Model file {filepath} not found")
        
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.is_trained = True
        
        print(f"Model loaded from {filepath}")
    
    def get_feature_importance(self):
        """Get feature importance from the trained model"""
        if not self.is_trained:
            raise ValueError("Model must be trained before getting feature importance")
        
        feature_names = [
            'project_area_sqft', 'num_floors', 'construction_type', 'location_urban',
            'complexity_score', 'materials_quality', 'labor_cost_per_sqft',
            'permits_and_fees', 'site_preparation_cost', 'utilities_cost',
            'project_duration_months'
        ]
        
        importance = self.model.feature_importances_
        feature_importance = pd.DataFrame({
            'feature': feature_names,
            'importance': importance
        }).sort_values('importance', ascending=False)
        
        return feature_importance

def main():
    """Main function to train and test the model"""
    print("Construction Budget Predictor - ML Model")
    print("=" * 50)
    
    # Initialize the predictor
    predictor = ConstructionBudgetPredictor()
    
    # Generate sample data
    print("Generating sample construction project data...")
    data = predictor.generate_sample_data(n_samples=2000)
    
    # Prepare features
    X, y = predictor.prepare_features(data)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")
    
    # Train the model
    print("\nTraining the model...")
    predictor.train(X_train, y_train)
    
    # Evaluate the model
    print("\nEvaluating the model...")
    results = predictor.evaluate(X_test, y_test)
    
    # Show feature importance
    print("\nFeature Importance:")
    feature_importance = predictor.get_feature_importance()
    print(feature_importance)
    
    # Save the model
    print("\nSaving the model...")
    predictor.save_model()
    
    # Test prediction with a sample project
    print("\nTesting prediction with a sample project...")
    sample_project = pd.DataFrame({
        'project_area_sqft': [5000],
        'num_floors': [3],
        'construction_type': [1],  # commercial
        'location_urban': [1],
        'complexity_score': [7.5],
        'materials_quality': [2],  # high
        'labor_cost_per_sqft': [120],
        'permits_and_fees': [15000],
        'site_preparation_cost': [25000],
        'utilities_cost': [12000],
        'project_duration_months': [12]
    })
    
    prediction = predictor.predict(sample_project)
    print(f"Predicted budget for sample project: ${prediction[0]:,.2f}")
    
    print("\nModel training and testing completed!")

if __name__ == "__main__":
    main() 