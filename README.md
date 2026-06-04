
Problem Statement

Modern computer networks generate massive volumes of traffic data, making it difficult for traditional security systems to accurately detect and respond to cyber threats in real time. Signature-based detection methods often fail to identify unknown or evolving attacks, while manual analysis is time-consuming and inefficient.
This project proposes an End-to-End Network Threat Detection and Classification Pipeline Using Isolation Forest and XGBoost. The system leverages Isolation Forest to detect anomalous network behavior and XGBoost to classify identified threats. By automating data preprocessing, anomaly detection, attack classification, and threat analysis, the pipeline aims to improve detection accuracy, reduce response time, and enhance overall network security against both known and unknown cyber attacks.

Project Objectives

To develop an end-to-end cybersecurity pipeline for automated network threat detection and classification.
To preprocess and analyze network traffic data for effective threat identification.
To use Isolation Forest for detecting anomalous network activities and potential cyber attacks.
To employ XGBoost for accurate classification of detected threats into attack categories.
To improve the accuracy and efficiency of cyber threat detection using machine learning techniques.
To provide real-time insights through visualizations and monitoring dashboards.
To reduce manual intervention in network security analysis and threat management.
To create a scalable and adaptable framework capable

Modules List

Data Collection Module
Collects network traffic and cybersecurity datasets.
Data Preprocessing Module
Cleans, transforms, encodes, and scales the data for model training.
Exploratory Data Analysis (EDA) Module
Analyzes traffic patterns, distributions, and attack trends.
Anomaly Detection Module (Isolation Forest)
Detects abnormal network behavior and suspicious activities.
Threat Classification Module (XGBoost)
Classifies detected anomalies into specific attack categories.
Model Evaluation Module
Measures performance using accuracy, precision, recall, F1-score, and confusion matrix.
Visualization & Monitoring Dashboard Module
Displays threat statistics, attack distributions, and model predictions.
Deployment Module
Deploys the complete end-to-end pipeline for real-time threat detection and analysis.

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
