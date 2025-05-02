# Titanic_Survival_Prediction

🚢 Titanic Survival Prediction using Data Science
This project focuses on predicting the survival of passengers aboard the RMS Titanic using data science techniques in a Jupyter Notebook. The model is trained using machine learning algorithms on the well-known Titanic dataset provided by Kaggle.

📌 Project Overview
The aim of this project is to:
* Perform exploratory data analysis (EDA) on the Titanic dataset.
* Clean and preprocess the data.
* Train machine learning models to predict passenger survival.
* Evaluate and compare model performances.
* Provide insights and visualizations to support predictions.

🧠 Technologies Used
* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib / Seaborn
* Scikit-learn
* Joblib (for saving the model)

📂 Project Structure

titanic_survival_prediction/
│
├── Titanic_Survival_Prediction.ipynb     # Main Jupyter notebook with full analysis
├── titanic_model.pkl                     # Trained machine learning model
├── app1.py                               # (Optional) Streamlit web app script
├── requirements.txt                      # List of dependencies
└── README.md                             # Project documentation

📊 Dataset
The dataset used is the Titanic - Machine Learning from Disaster dataset from Kaggle.
Kaggle Dataset Link:https://www.kaggle.com/datasets/yasserh/titanic-dataset

The dataset contains features like:
* PassengerId
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked
* Survived (target variable)

🚀 How to Run
- Clone this repository:
  git clone https://github.com/AnanyaB-262005/titanic_survival_prediction.git
  cd titanic_survival_prediction

- Install dependencies:
  pip install -r requirements.txt
  
- Open the Jupyter Notebook:
  jupyter notebook Titanic_Survival_Prediction.ipynb
  
- (Optional) Run the Streamlit app:
   streamlit run app1.py

✅ Results
Accuracy: 100%
Cross-Validation Score: 100%
The model performed perfectly on the test dataset, although further validation may be necessary to confirm generalizability.

Insights:
 * Women had higher survival chances.
 * Passengers in 1st class were more likely to survive.
 * Age and family aboard were significant factors.

📌 Future Improvements
* Hyperparameter tuning using GridSearchCV.
* Model ensemble and stacking.
* Deploy model to a cloud platform (e.g., Streamlit, Heroku).
* Build a REST API using Flask or FastAPI.
