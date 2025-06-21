import pandas as pd
from ml_model import ConstructionBudgetPredictor

# Feature prompts and their types
feature_prompts = [
    ("project_area_sqft", float, "Project area in square feet (e.g., 5000): "),
    ("num_floors", int, "Number of floors (e.g., 3): "),
    ("construction_type", str, "Construction type [residential/commercial/industrial]: "),
    ("location_urban", int, "Is the location urban? [1 for Yes, 0 for No]: "),
    ("complexity_score", float, "Complexity score (1-10): "),
    ("materials_quality", str, "Materials quality [low/medium/high]: "),
    ("labor_cost_per_sqft", float, "Labor cost per sqft (e.g., 120): "),
    ("permits_and_fees", float, "Permits and fees (e.g., 15000): "),
    ("site_preparation_cost", float, "Site preparation cost (e.g., 25000): "),
    ("utilities_cost", float, "Utilities cost (e.g., 12000): "),
    ("project_duration_months", float, "Project duration in months (e.g., 12): ")
]

# Categorical mappings
construction_type_map = {'residential': 0, 'commercial': 1, 'industrial': 2}
materials_quality_map = {'low': 0, 'medium': 1, 'high': 2}

def get_user_input():
    user_data = {}
    for key, typ, prompt in feature_prompts:
        while True:
            val = input(prompt)
            try:
                if key == 'construction_type':
                    val = val.lower()
                    if val not in construction_type_map:
                        raise ValueError()
                    user_data[key] = construction_type_map[val]
                elif key == 'materials_quality':
                    val = val.lower()
                    if val not in materials_quality_map:
                        raise ValueError()
                    user_data[key] = materials_quality_map[val]
                else:
                    user_data[key] = typ(val)
                break
            except Exception:
                print(f"Invalid input for {key}. Please try again.")
    return user_data

def main():
    print("\n--- Construction Budget Predictor: User Input Test ---\n")
    predictor = ConstructionBudgetPredictor()
    predictor.load_model()  # Loads from default path

    user_data = get_user_input()
    df = pd.DataFrame([user_data])
    prediction = predictor.predict(df)
    print(f"\nPredicted construction budget: ${prediction[0]:,.2f}\n")

if __name__ == "__main__":
    main() 