# ✋ Gesture Control Game

This project implements a gesture-controlled game using machine learning for gesture recognition. Players can control the game using hand gestures captured through their webcam.

## 🚀 Deployment

The live API is deployed on **Railway** and available at:

📎 **[Production URL](https://mlops-final-project-production-2c88.up.railway.app/docs)**

---

## 🌳 Git Branching Strategy

- **`master`**: This is the **production branch**, representing the deployed and stable state of the API. All final changes are merged here after testing.
- **`research`**: This branch contains **experimentation code** including model training, EDA, preprocessing logic, and MLflow tracking.
- **`api`**: This branch hosts the **FastAPI backend**, Prometheus integration, and other deployable code.

I forked the original MLOps course repository and began development using the `master` branch as my stable production line. Feature development and model iterations were done in `research`, while API and system monitoring infrastructure were developed in the `api` branch.

---

## 🧠 Project Objective

The objective of this project is to build a production-grade pipeline for classifying hand gestures using preprocessed MediaPipe hand landmarks.

---

## 🛠 Tech Stack

- **Python 3.10**
- **FastAPI** – API for real-time gesture classification.
- **XGBoost** – Classification model.
- **MediaPipe** – For extracting 3D hand landmarks.
- **MLflow** – Model tracking and experiment logging.
- **Prometheus + Grafana** – Monitoring metrics (e.g., latency, requests).
- **Docker + Docker Compose** – For containerized deployment.
- **Railway** – Cloud deployment.

---

## 🚀 Quick Start

1. Install the Live Server extension in VS Code:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Live Server"
   - Install the extension by Ritwick Dey

2. Launch the project:
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - The game should open in your default browser at `http://localhost:5500`

## 📁 Project Structure

- `index.html` - Main game interface
- `api-call.js` - ML model API integration
- `cam.js` - Webcam handling and gesture processing
- `keyboard.js` - Keyboard controls implementation
- `maze.js` - Maze game logic
- `mp.js` - Media processing utilities

---

## 🧪 ML Model Workflow

### 1. Data Preprocessing

- Hand landmark normalization (based on wrist and middle fingertip).
- Z-coordinates were **kept unnormalized**.
- Saved to `normalized_hagrid.csv`.

---

### 2\. Model Training

-   Input features: 63 values (x & y normalized, z kept raw).

-   Algorithm: `XGBoostClassifier`.

-   Labels encoded using `LabelEncoder`.

-   Model and encoder saved as `.pkl` files.

-   Logged with **MLflow** for experiment tracking.

---

### 3\. Custom Label Mapping

To simplify the final output:

python

Copy code

`custom_label_map = {
    "one": "left",
    "two_up": "up",
    "three": "down",
    "four": "right"
}`

---

📦 API Functionality
--------------------

### **POST /predict**

-   Input: JSON object containing 63 float values (MediaPipe hand landmarks).

-   Output: One of the following predictions:

    -   `left`

    -   `right`

    -   `up`

    -   `down`

    -   `unknown`

### **/metrics**

-   Exposes Prometheus-compatible metrics:

    -   `prediction_requests_total`

    -   `prediction_latency_seconds`

---

🔁 CI/CD with GitHub Actions
----------------------------

A full **CI/CD pipeline** is implemented using **GitHub Actions**. Every push or merge to the production branch triggers:

-   ✅ Linting & syntax checks

-   ✅ API testing (via test suite)

-   ✅ Automatic deployment to **Railway**

---

🐳 Run Locally with Docker Compose
----------------------------------

bash

CopyEdit

`git clone https://github.com/your-username/mlops-final-project.git
cd mlops-final-project
docker-compose up --build`

Once running:

-   API Docs: <http://localhost:8000/docs>

-   Prometheus: <http://localhost:9090>

-   Grafana: <http://localhost:3000>

---

## 🎮 Controls

The game can be controlled through:
- Hand gestures (via webcam)
- Keyboard arrows (as fallback)

---

👤 Author
---------

-   **Name**: Mohamed Mohy

-   **Institute**: ITI -- Machine Learning & AI Track

-   **Year**: 2025


