# 🏗️ Construction Budget Predictor

A powerful Machine Learning application that predicts construction project budgets using advanced algorithms and real-world construction parameters.

## 🌐 **Live Demo**
**[🚀 Try the App Now](https://construction-budget-predictor.streamlit.app/)**

## 📋 Table of Contents
- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The Construction Budget Predictor is an intelligent ML system designed to estimate construction project costs with high accuracy. It uses a Random Forest Regressor trained on comprehensive construction data to provide reliable budget predictions for various project types.

### 🚀 Key Capabilities
- **Real-time Budget Estimation** 💰
- **Multiple Project Types** 🏢🏠🏭
- **Interactive Web Interface** 🌐
- **High Accuracy Predictions** 📊
- **Feature Importance Analysis** 🔍

## 🌐 Live Demo

**🎯 [Try the Construction Budget Predictor Now!](https://construction-budget-predictor.streamlit.app/)**

Experience the app live with:
- Interactive form inputs
- Real-time budget predictions
- Professional UI/UX
- Instant results

*No installation required - just click and start predicting!*

## ✨ Features

### 🎛️ Input Parameters
- **Project Area** 📏 - Square footage of the construction
- **Number of Floors** 🏢 - Building height and complexity
- **Construction Type** 🏗️ - Residential, Commercial, or Industrial
- **Location Type** 🌆 - Urban or Rural setting
- **Complexity Score** 📈 - Project difficulty (1-10 scale)
- **Materials Quality** 🎨 - Low, Medium, or High grade
- **Labor Costs** 👷 - Cost per square foot
- **Permits & Fees** 📋 - Regulatory costs
- **Site Preparation** 🚧 - Land preparation expenses
- **Utilities Cost** ⚡ - Infrastructure setup
- **Project Duration** ⏱️ - Timeline in months

### 📊 Model Performance
- **R² Score**: 0.9387 (93.87% accuracy)
- **Mean Absolute Error**: $509,489.39
- **Root Mean Square Error**: $735,572.63

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the Repository** 📥
   ```bash
   git clone https://github.com/Swamniathan-04/Construction-Budget-Predictor.git
   cd Construction-Budget-Predictor
   ```

2. **Install Dependencies** 📦
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation** ✅
   ```bash
   python -c "import streamlit, pandas, sklearn; print('✅ All dependencies installed successfully!')"
   ```

## 🚀 Usage

### Method 1: Live Web App (Recommended) 🌐
**[🚀 Access the Live App](https://construction-budget-predictor.streamlit.app/)**

1. **Open the link above**
2. **Enter your project details**
3. **Click "Predict Budget"**
4. **Get instant results!**

### Method 2: Local Web Interface 🌐

1. **Start the Streamlit App**
   ```bash
   python -m streamlit run predict_with_ui.py
   ```

2. **Open Your Browser**
   - Navigate to: `http://localhost:8501`
   - You'll see a beautiful, interactive interface

3. **Enter Project Details**
   - Fill in all the required fields
   - Adjust sliders and select options
   - Click "Predict Budget" to get instant results

### Method 3: Command Line Interface 💻

1. **Run the Prediction Script**
   ```bash
   python predict_with_input.py
   ```

2. **Follow the Prompts**
   - Enter project area, number of floors, etc.
   - Choose construction type and materials quality
   - Get your budget prediction

### Method 4: Train Your Own Model 🧠

1. **Run the Training Script**
   ```bash
   python ml_model.py
   ```

2. **View Results**
   - Model performance metrics
   - Feature importance analysis
   - Sample predictions

## 🧠 Model Details

### Algorithm
- **Random Forest Regressor** 🌲
- **100 Estimators** for robust predictions
- **Standard Scaler** for feature normalization

### Feature Engineering
- **Categorical Encoding** for construction types and materials
- **Feature Scaling** for numerical variables
- **Noise Addition** for realistic data simulation

### Training Data
- **2000 Sample Projects** generated with realistic parameters
- **11 Input Features** covering all major cost factors
- **80/20 Train-Test Split** for reliable evaluation

## 📁 Project Structure

```
Construction-Budget-Predictor/
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 🧠 ml_model.py                  # Main ML model and training
├── 🌐 predict_with_ui.py           # Streamlit web interface
├── 💻 predict_with_input.py        # Command line interface
├── 💾 construction_budget_model.pkl # Trained model file
└── 📊 blueberry/                   # Legacy web app (removed)
```

## 🔧 API Reference

### ConstructionBudgetPredictor Class

```python
from ml_model import ConstructionBudgetPredictor

# Initialize predictor
predictor = ConstructionBudgetPredictor()

# Train model
predictor.train(X_train, y_train)

# Make predictions
prediction = predictor.predict(X)

# Evaluate model
results = predictor.evaluate(X_test, y_test)

# Save/Load model
predictor.save_model('model.pkl')
predictor.load_model('model.pkl')

# Get feature importance
importance = predictor.get_feature_importance()
```

### Key Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `train(X, y)` | Train the model | None |
| `predict(X)` | Make predictions | Array |
| `evaluate(X, y)` | Evaluate performance | Dict |
| `save_model(path)` | Save trained model | None |
| `load_model(path)` | Load saved model | None |

## 🎨 Customization

### Adding New Features
1. Modify the `generate_sample_data()` method in `ml_model.py`
2. Update feature columns in `prepare_features()`
3. Retrain the model with new data

### Adjusting Model Parameters
```python
# In ml_model.py, modify the RandomForestRegressor
self.model = RandomForestRegressor(
    n_estimators=200,  # More trees
    max_depth=15,      # Control tree depth
    random_state=42
)
```

## 🧪 Testing

### Run All Tests
```bash
# Test model training
python ml_model.py

# Test command line interface
python predict_with_input.py

# Test web interface
python -m streamlit run predict_with_ui.py
```

### Sample Test Cases
- **Small Residential**: 2,000 sqft, 2 floors, low complexity
- **Medium Commercial**: 10,000 sqft, 5 floors, medium complexity
- **Large Industrial**: 50,000 sqft, 1 floor, high complexity

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository** 🍴
2. **Create a Feature Branch** 🌿
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make Your Changes** ✏️
4. **Test Thoroughly** 🧪
5. **Submit a Pull Request** 📤

### Contribution Guidelines
- Add comprehensive tests for new features
- Update documentation for API changes
- Follow PEP 8 style guidelines
- Include emojis in commit messages! 😄

## 📈 Future Enhancements

- [ ] **Deep Learning Models** 🧠
- [ ] **Real-time Data Integration** 🔄
- [ ] **Mobile App** 📱
- [ ] **Multi-language Support** 🌍
- [ ] **Advanced Analytics Dashboard** 📊
- [ ] **Cost Breakdown Analysis** 💸
- [ ] **Project Timeline Estimation** ⏰
- [ ] **Risk Assessment** ⚠️

## 🐛 Troubleshooting

### Common Issues

**Issue**: Streamlit not found
```bash
# Solution: Install streamlit
pip install streamlit
```

**Issue**: Model file not found
```bash
# Solution: Train the model first
python ml_model.py
```

**Issue**: Port 8501 already in use
```bash
# Solution: Use different port
streamlit run predict_with_ui.py --server.port 8502
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Scikit-learn** for the ML algorithms
- **Streamlit** for the beautiful web interface
- **Pandas** for data manipulation
- **NumPy** for numerical computations

## 📞 Support

- **Live App**: [https://construction-budget-predictor.streamlit.app/](https://construction-budget-predictor.streamlit.app/)
- **GitHub**: [https://github.com/Swamniathan-04/Construction-Budget-Predictor](https://github.com/Swamniathan-04/Construction-Budget-Predictor)
- **Issues**: [GitHub Issues](https://github.com/Swamniathan-04/Construction-Budget-Predictor/issues)

---

<div align="center">

**Made with ❤️ for the Construction Industry**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Available-brightgreen.svg)](https://construction-budget-predictor.streamlit.app/)

</div> 