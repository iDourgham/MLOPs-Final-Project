Here is the updated version of your research project documentation with the new model scores and a justification for choosing XGBoost:

---

# Research: Hand Gesture Classification

This repository contains the implementation, training, and evaluation of machine learning models for **Hand Gesture Classification** using a normalized dataset derived from the HaGRID dataset. The goal is to classify different hand gestures accurately using various classification algorithms.

---

## Project Overview

Hand gesture recognition is an important area in computer vision and human-computer interaction. This project focuses on classifying hand gestures from normalized landmark data using classical and ensemble machine learning models.

The project includes:

* Data preprocessing and label encoding
* Model training using Random Forest, Support Vector Classifier (SVC), and XGBoost classifiers
* Evaluation using accuracy, precision, recall, and F1-score metrics
* Confusion matrix visualization
* Model logging and experiment tracking with MLflow

---

## Dataset

The dataset is a CSV file containing 4 Hand Signs features and a target label column. The label column is encoded into numerical classes for training.

---

# Hand Gesture Classification Models Comparison

This repository contains implementations and experiments for classifying hand gestures using various machine learning models. Below is a comparison of the performance metrics of three different models trained and evaluated on the same dataset.

| Model         | Accuracy   | F1 Score   | Precision  | Recall     |
| ------------- | ---------- | ---------- | ---------- | ---------- |
| Random Forest | 0.9859     | 0.9865     | 0.9866     | 0.9864     |
| SVC           | **0.9877** | **0.9882** | **0.9888** | **0.9878** |
| XGBoost       | 0.9868     | 0.9874     | 0.9878     | 0.9872     |

---

## Summary

* **SVC** achieved the highest performance across all metrics, making it the most accurate model in raw numbers.
* **XGBoost** performed almost equally well and maintained robust generalization, with only a marginal drop in accuracy.
* **Random Forest** also showed excellent results, slightly behind XGBoost.

---

## Model Selection Justification

Despite SVC slightly outperforming XGBoost in accuracy, the chosen model for deployment is **XGBoost**. This decision is based on several practical considerations:

* **XGBoost is significantly faster** during both training and inference, especially on large datasets.
* It offers **better support for handling missing values** and built-in regularization to prevent overfitting.
* XGBoost integrates easily into production pipelines and scales well in distributed environments.
* It is overall **lighter and more flexible**, making it a better choice for deployment where resources and latency are concerns.

---

## Notes

* All models were trained on the same preprocessed dataset of normalized hand gesture features.
* Metrics were computed on the same test set to ensure fair comparison.
* Performance metrics used:

  * **Accuracy**: Overall correctness of the model.
  * **F1 Score**: Harmonic mean of precision and recall.
  * **Precision**: Correct positive predictions over all positive predictions.
  * **Recall**: Correct positive predictions over all actual positives.

---

## Installation

To run the code and experiments, ensure you have the following Python packages installed:

---

## Setup Instructions

### 3. Create the environment

You can set up the required environment either with Conda or pip.

#### Using Conda (recommended):

```bash
conda env create -f environment.yml
conda activate mediapipe_env
```

### Requirements

```bash
mlflow==2.22.0
scipy==1.15.2
psutil==5.9.0
numpy==1.26.4
pandas==2.2.3
seaborn==0.13.2
mediapipe==0.10.21
cv2==4.11.0
xgboost==2.1.1
scikit-learn==1.6.1
```

---

## Contributors

* **Mohamed Mohy** ([GitHub Profile](https://github.com/iDourgham))
  ([LinkedIn Profile](https://www.linkedin.com/in/eng-m-mohy/))

---