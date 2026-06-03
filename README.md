END-TO-END CYBER THREAT DETECTION PIPELINE USING ISOLATION FOREST AND XGBOOST is an AI-powered cybersecurity solution designed to detect, classify, and explain network anomalies in real time. Inspired by the human immune system, the project continuously monitors network traffic, identifies suspicious activities, and provides actionable insights for threat mitigation.

The system uses Isolation Forest for anomaly detection and XGBoost for attack classification, enabling accurate identification of malicious network behavior. To improve transparency and trust, SHAP (SHapley Additive Explanations) is integrated to explain model predictions and highlight the key factors behind each decision.

An interactive dashboard built with Streamlit and Plotly allows users to visualize anomalies, attack trends, and model outputs through dynamic charts and reports. The project is trained and evaluated using the KDD Cup 99 network intrusion dataset and is deployed using Hugging Face Spaces for easy accessibility.

This project demonstrates the integration of Machine Learning, Explainable AI, and Cybersecurity to create an intelligent and scalable threat detection system.

**Frontend**

The frontend is developed using Streamlit, providing an interactive dashboard for monitoring network activity. Plotly is used to create dynamic charts and visualizations for anomaly and attack analysis.

**Backend**

The backend is built with Python and handles data preprocessing, anomaly detection, attack classification, and result generation. Machine learning models are implemented using Scikit-learn, XGBoost, and SHAP.

**Database / Dataset**

The system uses the KDD Cup 99 network intrusion dataset. Instead of a traditional database, data is managed in memory using Pandas DataFrames for efficient processing.

AI & Machine Learning

The AI engine consists of multiple machine learning components working together:

Isolation Forest is used as the primary anomaly detection model. It identifies unusual network behavior by isolating data points that significantly differ from normal traffic patterns.
XGBoost is employed to classify detected anomalies into specific attack categories, improving the system's ability to distinguish between different types of cyber threats.
SHAP (SHapley Additive Explanations) provides model interpretability by highlighting the features that most influenced a prediction. This enables users to understand why a particular network activity was classified as suspicious.
The combination of anomaly detection, attack classification, and explainable AI creates a robust and transparent cybersecurity monitoring system.
Deployment

The project follows a cloud-based deployment workflow:

Google Colab was used for model development, experimentation, and training due to its accessible cloud computing resources.
Ngrok was utilized during development to create a secure public tunnel, allowing external access to the locally hosted Streamlit application for testing and demonstration purposes.
Hugging Face Spaces serves as the final deployment platform, hosting the Streamlit application and making it accessible through a web interface without requiring local installation.
