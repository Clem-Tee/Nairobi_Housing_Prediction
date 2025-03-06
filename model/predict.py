import pandas as pd
import joblib
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge

# Load the dataset for training
df = pd.read_csv("data/rent_apts.csv")

# Data cleaning
df.dropna(subset=["sq_mtrs", "Bedrooms", "Bathrooms"], inplace=True)
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)
df["Neighborhood"] = df["Neighborhood"].apply(lambda x: x.split(",")[-1].strip())
df = df[(df["sq_mtrs"] >= 20) & (df["sq_mtrs"] <= 400)]

# Train the model
features = ["sq_mtrs", "Bedrooms", "Bathrooms", "Neighborhood"]
X_train = df[features]
y_train = df["Price"]

model = make_pipeline(
    OneHotEncoder(handle_unknown="ignore", sparse_output=False),
    SimpleImputer(),
    Ridge()
)

model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "model/trained_model.pkl")

def predict_price(sq_mtrs, bedrooms, bathrooms, neighborhood):
    """Predict the house rental price based on input features."""
    model = joblib.load("model/trained_model.pkl")
    data = pd.DataFrame([[sq_mtrs, bedrooms, bathrooms, neighborhood]], columns=features)
    predicted_price = model.predict(data)[0]
    return predicted_price
