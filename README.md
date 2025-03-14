# 🏡 Nairobi Apartment Price Prediction 💰

This project predicts apartment rental prices in Nairobi based on features such as neighborhood, number of bedrooms, and bathrooms.

## 🚀 Tech Stack  
- **Python** 🐍  
- **Pandas, NumPy, Seaborn** 📊  
- **Scikit-learn** 🤖  
- **Random Forest Regression** 🌳  

## 📜 Dataset  
The dataset contains apartment rental listings with the following features:  
- **Neighborhood** (categorical)  
- **Bedrooms** (numerical)  
- **Bathrooms** (numerical)  
- **Price (KES)** (target variable)  

## 📈 Model Performance  
- **Baseline MAE:** 33,232 KES  
- **Trained Model MAE:** 24,052 KES (27% improvement 🎯)  

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/Clem-Tee/nairobi_apartment_prediction.git
cd nairobi_apartment_prediction
```  

### 2️⃣ Create a Virtual Environment & Install Dependencies  
```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```  

### 3️⃣ Create Required Directories  
```sh
mkdir models
```  
> **Note:** The `models/` directory is ignored in Git to prevent tracking large files. You must create it manually before training the model.

## 📊 Usage  

### 1️⃣ Train the Model  
```sh
python src/train_model.py
```  
After training, the model will be saved in the `models/` directory.  

### 2️⃣ Predict Apartment Prices  
```sh
python src/predict.py
```  
The script will prompt you to enter:  
✔ **Neighborhood** (e.g., "Westlands")  
✔ **Bedrooms** (e.g., "2")  
✔ **Bathrooms** (e.g., "2")  

It then predicts the apartment price based on the trained model.  

## 🛠 Project Structure  
```bash
nairobi_apartment_prediction/
│── data/                # Contains the dataset (ignored in Git)
│── models/              # Stores trained models (ignored in Git)
│── src/                 # Source code
│   ├── train_model.py   # Training script
│   ├── predict.py       # Prediction script
│   ├── utils.py         # Input validation functions
│── .gitignore           # Ignore unnecessary files
│── LICENSE              # MIT License
│── README.md            # Project documentation
│── requirements.txt     # Dependencies
```  

## ⚖️ License  
© 2025 Clement Ogol. All Rights Reserved.  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

## ⭐ Contribute & Support  
If you find this project useful, please ⭐ star the repository!  
Feel free to contribute by submitting pull requests or reporting issues.  

🚀 **Happy Coding!**  
