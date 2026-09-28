# Diabetes Prediction using Logistic Regression

## Project Overview

This project uses **Machine Learning and Logistic Regression** to predict whether a person is likely to have diabetes based on medical and demographic features.

The project includes data preprocessing, exploratory data analysis (EDA), visualization, model training, evaluation, and deployment using Streamlit.

## Dataset

The dataset contains the following features:

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age
* Outcome

### Target Variable

**Outcome**

* `0` → No Diabetes
* `1` → Diabetes

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## Project Workflow

### 1. Data Loading

The diabetes dataset is loaded using Pandas.

### 2. Data Preprocessing

The dataset is checked for:

* Missing values
* Invalid zero values
* Data types
* Statistical information

Zero values in medical features such as Glucose, BloodPressure, SkinThickness, Insulin, and BMI are treated as missing values where appropriate.

### 3. Exploratory Data Analysis

The following visualizations are performed:

* Histograms
* Boxplots
* Correlation Heatmap
* Pairplot
* Target variable distribution

### 4. Data Preparation

The data is divided into:

* Training data
* Testing data

Missing values are handled using median imputation, and numerical features are standardized using `StandardScaler`.

### 5. Machine Learning Model

**Logistic Regression** is used as the classification algorithm.

The model predicts whether the patient belongs to:

* Class 0 → No Diabetes
* Class 1 → Diabetes

### 6. Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* Confusion Matrix
* ROC Curve

### 7. Model Deployment

The trained model is saved using Joblib:

```python
joblib.dump(model_pipeline, "diabetes_logistic_model.pkl")
```

A **Streamlit application** is created to allow users to enter patient information and receive a diabetes prediction.

## Project Structure

```text
Diabetes-Logistic-Regression/
│
├── Diabetes_Logistic_Regression.ipynb
├── diabetes.csv
├── diabetes_logistic_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Model Output

The Streamlit application accepts the patient's information and displays:

* **Diabetes Predicted**, or
* **No Diabetes Predicted**

## Future Improvements

* Try other classification algorithms such as Random Forest, SVM, and KNN.
* Perform hyperparameter tuning.
* Compare different models.
* Improve the Streamlit user interface.
* Deploy the application online using Streamlit Community Cloud.

## Author

**Shivadeep**

This project was developed as part of a Machine Learning/Data Analytics learning project.
https://diabetespredictionusinglogisticregressionml.streamlit.app/
