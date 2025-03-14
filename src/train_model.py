import warnings
import pandas as pd
import joblib

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error

warnings.simplefilter(action="ignore", category=FutureWarning)

# Load dataset
df = pd.read_csv("data/rent_apts.csv")

# Clean data
df.dropna(subset=["sq_mtrs", "Bedrooms", "Bathrooms"], inplace=True)
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(int)
df["Neighborhood"] = df["Neighborhood"].apply(lambda x: x.split(",")[-1].strip())
df.drop(columns=["sq_mtrs", "link", "Agency"], inplace=True)

# Define target and features
target = "Price"
features = ["Neighborhood", "Bedrooms", "Bathrooms"]

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Neighborhood'])
    ],
    remainder='passthrough'
)

# Create pipeline
pipeline = make_pipeline(
    preprocessor,
    RandomForestRegressor(n_estimators=100, random_state=42)
)

# Train model
pipeline.fit(X_train, y_train)

# Evaluate model
y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Model MAE: {mae:.2f}")

# Save model
joblib.dump(pipeline, "models/apartment_price_model.pk1")
print("Model saved successfully!")
