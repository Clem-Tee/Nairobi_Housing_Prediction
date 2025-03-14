🏡 Nairobi Apartment Price Prediction
An AI-powered model to predict apartment rental prices in Nairobi using Machine Learning.

🚀 Tech Stack
Python: Utilizes libraries like Pandas, NumPy, and Seaborn for data manipulation and visualization.

Scikit-learn: Employs machine learning capabilities, specifically Random Forest Regression.

Joblib: Used for model persistence to ensure efficient model loading and saving.

📜 Dataset Overview
This project analyzes apartment rental prices in Nairobi based on key features:

Neighborhood: The location of the apartment.

Bedrooms: Number of bedrooms.

Bathrooms: Number of bathrooms.

Price (KES): The target variable for prediction.

📈 Model Performance
Baseline MAE: 33,232 KES

Trained Model MAE: 24,052 KES (27% Improvement 🎯)

🔧 Installation & Setup
1️⃣ Clone the Repository

text
git clone https://github.com/yourusername/nairobi_apartment_prediction.git
cd nairobi_apartment_prediction
2️⃣ Create a Virtual Environment & Install Dependencies

text
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
3️⃣ Create Required Directories

text
mkdir models
Note: The models/ directory is ignored in Git to prevent tracking large files. You must create it manually before training the model.

📊 Usage
1️⃣ Train the Model
text
python src/train_model.py
2️⃣ Predict Apartment Prices
text
python src/predict.py
🛠 Project Structure
text
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
⚖️ License
© 2025 Clement Ogol. All Rights Reserved.
This project is licensed under the MIT License. See the LICENSE file for details.

⭐ Contribute & Support
If you find this project useful, please ⭐ star the repository!
Feel free to contribute by submitting pull requests or reporting issues.
