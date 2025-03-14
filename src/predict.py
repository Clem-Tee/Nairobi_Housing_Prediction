import joblib
import sys
import pandas as pd

from utils import validate_input

# Load trained model
model = joblib.load("models/apartment_price_model.pk1")

# Get user input
neighborhood = input("Enter neighborhood: ").strip()
bedrooms = input("Enter number of bedrooms: ").strip()
bathrooms = input("Enter number of bathrooms: ").strip()

# Validate input
valid, message = validate_input(neighborhood, bedrooms, bathrooms)
if not valid:
    print(f"Error: {message}")
    sys.exit()

# Convert inputs to correct data types
bedrooms = int(bedrooms)
bathrooms = int(bathrooms)

# Prepare input data
data = pd.DataFrame([[neighborhood, bedrooms, bathrooms]], columns=["Neighborhood", "Bedrooms", "Bathrooms"])

# Predict price
predicted_price = model.predict(data)[0]
print(f"Estimated Apartment Price: {round(predicted_price, 2)} KES")
