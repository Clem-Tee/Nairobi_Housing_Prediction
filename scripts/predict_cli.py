import argparse
from model.predict import predict_price

def main():
    parser = argparse.ArgumentParser(description="Nairobi House Price Prediction CLI")
    
    parser.add_argument("--sq_mtrs", type=float, required=True, help="Apartment size in square meters (20-400)")
    parser.add_argument("--bedrooms", type=int, required=True, help="Number of bedrooms (1-6)")
    parser.add_argument("--bathrooms", type=int, required=True, help="Number of bathrooms (1-6)")
    parser.add_argument("--neighborhood", type=str, required=True, help="Neighborhood name")

    args = parser.parse_args()

    # Validate inputs
    if not (20 <= args.sq_mtrs <= 400):
        print("Error: Size must be between 20 and 400 square meters.")
        return
    if not (1 <= args.bedrooms <= 6):
        print("Error: Bedrooms must be between 1 and 6.")
        return
    if not (1 <= args.bathrooms <= 6):
        print("Error: Bathrooms must be between 1 and 6.")
        return

    # Make prediction
    predicted_price = predict_price(args.sq_mtrs, args.bedrooms, args.bathrooms, args.neighborhood)
    print(f"\nEstimated Rent Price: KSh {predicted_price:,.2f}")

if __name__ == "__main__":
    main()
