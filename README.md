# OptiCrop - Smart Agricultural Production Optimization Engine

OptiCrop is a machine learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. It helps farmers make data-driven decisions to improve agricultural productivity and resource utilization.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open%20Application-brightgreen?style=flat-square&logo=render&logoColor=white)](https://opticrop-2-s4l5.onrender.com/)

---

## Features

- Crop recommendation using Machine Learning
- Predicts the best crop based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - Soil pH
  - Rainfall
- Data Analysis and Visualization
- Logistic Regression-based prediction model
- Flask web application

---

## Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Flask (Python)

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

---

## Project Structure

```
OptiCrop/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── notebook.ipynb
│
└── dataset/
    └── Crop_recommendation.csv
```

---

## Installation

Clone the repository

```bash
git clone 
```

Move into the project directory

```bash
cd OptiCrop
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment


```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Exploratory Data Analysis
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Model Serialization (`model.pkl`)
8. Flask Deployment

---

## Model Performance

| Metric    | Score     |
|-----------|-----------|
| Accuracy  | **96.76%** |
| Precision | **0.969** | 
| Recall    | **0.9676** |
| F1-Score  | **0.9677** |

The trained Logistic Regression model achieved an overall accuracy of **96.76%**, demonstrating reliable crop recommendation performance.

---

## Input Parameters

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

---

## Output

The application predicts the most suitable crop for cultivation based on the given soil and environmental conditions.