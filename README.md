# Heart Disease Predictor

This project aims to predict the likelihood of heart disease using machine learning techniques. The model is trained on a dataset comprising over 300,000 records, leveraging advanced data analysis and machine learning pipelines to ensure high performance and scalability. The project also incorporates a Streamlit application for easy production deployment.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Modeling Approach](#modeling-approach)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)

## Project Overview
This project focuses on developing a comprehensive **Heart Disease Predictor** by analyzing a large dataset to uncover trends and build predictive models. The key goals were:
- Thorough data analysis to understand underlying patterns.
- Effective handling of imbalanced data.
- Building scalable and efficient machine learning pipelines.
- Deploying the model using **Streamlit** for an interactive user experience.

## Dataset
The dataset used for this project consists of **over 300,000 records** with various features, including demographic information, medical history, and lifestyle choices, which are pertinent to predicting heart disease risk.

## Features
- **Univariate and Bivariate Analysis**: To uncover patterns and relationships in the data.
- **Imbalanced Data Handling**: Managed using the **IBM-Learn** library to balance the dataset and improve model performance.
- **Streamlined Machine Learning Pipelines**: Preprocessing both categorical and numerical data for efficient modeling.
- **Streamlit Application**: The predictor is deployed with Streamlit for a user-friendly interface.

## Technologies Used
- **Python**: The core programming language.
- **Pandas**: For data manipulation and analysis.
- **IBM-Learn**: For handling imbalanced datasets.
- **Scikit-learn**: For building machine learning models.
- **Streamlit**: For deploying the model as a web application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-disease-predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd heart-disease-predictor
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Upload your dataset or use the default one provided.
3. Input relevant features and get predictions for heart disease risk.

## Modeling Approach
- **Data Preprocessing**: Data cleaning, handling missing values, and scaling were performed for numerical features, while categorical features were one-hot encoded.
- **Univariate & Bivariate Analysis**: Conducted to identify relationships and imbalances within the data.
- **Machine Learning Pipelines**: Built streamlined pipelines that preprocess data and fit models for efficient prediction and scalability.
- **Handling Imbalanced Data**: Used the **IBM-Learn** library to manage class imbalance and improve the model’s predictive performance.

## Results
The model demonstrates high accuracy in predicting heart disease, overcoming challenges posed by imbalanced data and large datasets. It is optimized for both performance and scalability.

## Future Work
- Enhancing model performance using more advanced techniques like deep learning.
- Adding more features to improve prediction accuracy.
- Enhancing the UI of the Streamlit application.
  
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
