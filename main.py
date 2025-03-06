import pandas as pd
from model.predict import predict_price

def main():
    print("Welcome to Nairobi House Price Prediction Model!")

    try:
        sq_mtrs = float(input("Enter apartment size in square meters (20 - 400): "))
        if sq_mtrs < 20 or sq_mtrs > 400:
            raise ValueError("Size must be between 20 and 400 sq meters.")

        bedrooms = int(input("Enter number of bedrooms (1 - 6): "))
        if bedrooms < 1 or bedrooms > 6:
            raise ValueError("Bedrooms must be between 1 and 6.")

        bathrooms = int(input("Enter number of bathrooms (1 - 6): "))
        if bathrooms < 1 or bathrooms > 6:
            raise ValueError("Bathrooms must be between 1 and 6.")

        neighborhood = input("Enter neighborhood: ").strip().title()

        # Make prediction
        predicted_price = predict_price(sq_mtrs, bedrooms, bathrooms, neighborhood)
        print(f"\nEstimated Rent Price: KSh {predicted_price:,.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
