import pandas as pd

# Load dataset for validation
df = pd.read_csv("data/rent_apts.csv")
valid_neighborhoods = set(df["Neighborhood"].apply(lambda x: x.split(",")[-1].strip()).unique())

def validate_input(neighborhood, bedrooms, bathrooms):
    if neighborhood not in valid_neighborhoods:
        return False, "Invalid Neighborhood. Choose from dataset."
    if not bedrooms.isdigit() or int(bedrooms) <= 0:
        return False, "Bedrooms must be a positive integer."
    if not bathrooms.isdigit() or int(bathrooms) <= 0:
        return False, "Bathrooms must be a positive integer."
    return True, ""
    