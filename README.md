# 🏡 Nairobi Apartment Price Prediction  

**An AI-powered model to predict apartment rental prices in Nairobi using Machine Learning.**  

---

## 🚀 Tech Stack  
✅ **Python** (Pandas, NumPy, Seaborn)  
✅ **Scikit-learn** (Machine Learning)  
✅ **Random Forest Regression**  
✅ **Joblib** (Model Persistence)  

---

## 📜 Dataset Overview  
This project analyzes apartment rental prices in Nairobi based on key features:  
✔ **Neighborhood** – The location of the apartment  
✔ **Bedrooms** – Number of bedrooms  
✔ **Bathrooms** – Number of bathrooms  
✔ **Price (KES)** – The target variable for prediction  

---

## 📈 Model Performance  
🔹 **Baseline MAE:** 33,232 KES  
🔹 **Trained Model MAE:** 24,052 KES (**27% Improvement 🎯**)  

---

## 🔧 Installation & Setup  

### **1️⃣ Clone the Repository** 
```sh
git clone https://github.com/yourusername/nairobi_apartment_prediction.git
cd nairobi_apartment_prediction

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```sh
# Create a virtual environment
python -m venv venv

```sh
# Activate the virtual environment
# On Windows:
venv\Scripts\activate

```sh
# On macOS/Linux:
source venv/bin/activate

```sh
# Install required packages
pip install -r requirements.txt

### **3️⃣ Create Required Directories**
```sh
mkdir models
Note: The models/ directory is ignored in Git to prevent tracking large files. You must create it manually before training the model.

## 📊 Usage
### **1️⃣ Train the Model**
```sh
python src/train_model.py

### **2️⃣ Predict Apartment Prices**
```sh
python src/predict.py

## 🛠 Project Structure
```sh
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

## ⚖️ License
© 2025 Clement Ogol. All Rights Reserved.
This project is licensed under the MIT License. See the LICENSE file for details.

## ⭐ Contribute & Support
If you find this project useful, please ⭐ star the repository!
Feel free to contribute by submitting pull requests or reporting issues.

## 🚀 Happy Coding!
