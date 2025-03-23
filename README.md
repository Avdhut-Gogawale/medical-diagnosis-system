# 🏥 AI-Powered Medical Diagnosis System

## 📊 Project Overview
This project is an **AI-powered medical diagnosis system** that predicts the likelihood of **Diabetes** and **Heart Disease** based on patient data. It uses machine learning models trained on medical datasets and provides easy access to predictions through a **Streamlit** web interface.

## 🛠️ Features
- **Diabetes Prediction**: Predicts whether a patient is diabetic based on clinical inputs.
- **Heart Disease Prediction**: Evaluates patient data to predict the likelihood of heart disease.
- **User-Friendly Interface**: Interactive web-based UI built with **Streamlit**.
- **Fast & Accurate**: Utilizes pre-trained models for rapid predictions.

## 📂 Project Structure
```
medical_diagnosis/
├── app.py                     # Main Streamlit application
├── diabetes_model.pkl         # Trained Diabetes model
├── heart_disease_model.pkl    # Trained Heart Disease model
├── diabetes_scaler.pkl        # Scaler for Diabetes inputs
├── heart_scaler.pkl           # Scaler for Heart inputs
├── diabetes_data.csv          # (Optional) Diabetes dataset
├── heart_disease_data.csv     # (Optional) Heart Disease dataset
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation
```

## 📋 Requirements
Ensure you have **Python 3.10+** installed on your system.

Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/medical_diagnosis.git
   cd medical_diagnosis
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

Access the web application at: `http://localhost:8501`

## 📊 Model Details
- **Diabetes Model**: Trained on the **PIMA Indian Diabetes Dataset**
- **Heart Disease Model**: Trained on a comprehensive heart disease dataset

## 📤 Deployment
You can deploy this project using **Streamlit Community Cloud**:
1. Push the project to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and log in.
3. Select your GitHub repository and deploy the `app.py` file.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues and submit pull requests.

## 📄 License
This project is open-source and available under the **MIT License**.
