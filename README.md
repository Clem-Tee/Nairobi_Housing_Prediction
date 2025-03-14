# Nairobi Apartment Price Prediction 🏡💰  

This project predicts apartment rental prices in Nairobi based on features like neighborhood, number of bedrooms, and bathrooms.  

## 🚀 Tech Stack  
- Python 🐍  
- Pandas, NumPy, Seaborn 📊  
- Scikit-learn 🤖  
- Random Forest Regression 🌳  

## 📜 Dataset  
The dataset contains apartment rental listings with features such as:  
- **Neighborhood** (categorical)  
- **Bedrooms** (numerical)  
- **Bathrooms** (numerical)  
- **Price (KES)** (target variable)  

## 📈 Model Performance  
- **Baseline MAE:** 33,232 KES  
- **Trained Model MAE:** 24,052 KES (27% improvement 🎯)  

## 🔧 Installation & Usage  
```sh
# Clone repository
git clone https://github.com/yourusername/nairobi_apartment_prediction.git
cd nairobi_apartment_prediction

# Install dependencies
pip install -r requirements.txt

# Train model
python src/train_model.py

# Predict price
python src/predict.py
