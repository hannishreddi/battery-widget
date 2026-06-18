# Battery Drain Prediction using Machine Learning

A machine learning project that predicts battery discharge rates using real-time system telemetry data collected from a Windows device. The project builds a custom dataset from system performance metrics, trains a Random Forest Regression model, and integrates predictions into a desktop widget for battery usage estimation.

## Overview

Battery consumption varies significantly depending on system workload and user activity. This project aims to model battery discharge behavior by collecting system-level metrics such as CPU usage, RAM utilization, network activity, running processes, and device usage context.

The collected data is used to train a machine learning model that predicts battery drain rates and estimates remaining battery life under different workloads.

## Features

* Real-time system telemetry collection
* Automatic workload context detection

  * Coding
  * Browsing
  * Gaming
  * Idle
* Custom dataset generation
* Feature engineering and preprocessing
* Random Forest Regression model
* Desktop widget for live predictions
* Battery drain rate estimation
* Remaining battery life calculation

## Project Structure

```text
battery-widget/
│
├── collector.py        # Collects system telemetry and creates dataset
├── train_model.py      # Trains Random Forest Regression model
├── widget.py           # Desktop widget with live predictions
├── data.csv            # Generated dataset
├── model.pkl           # Trained ML model
├── encoder.pkl         # Label encoder for context feature
└── README.md
```

## Dataset Features

The dataset contains the following features:

| Feature   | Description                              |
| --------- | ---------------------------------------- |
| cpu       | CPU utilization percentage               |
| ram       | RAM utilization percentage               |
| battery   | Current battery percentage               |
| plugged   | Charging status                          |
| processes | Number of running processes              |
| net_sent  | Network bytes sent                       |
| net_recv  | Network bytes received                   |
| top_cpu   | Highest CPU-consuming process            |
| context   | User activity context                    |
| drain     | Battery discharge rate (target variable) |

## Machine Learning Pipeline

### Data Collection

System telemetry is collected using the `psutil` library.

The collector records:

* CPU usage
* Memory usage
* Battery percentage
* Charging status
* Network activity
* Running processes
* Active workload context

### Context Detection

The system automatically categorizes user activity into:

* Coding
* Browsing
* Gaming
* Idle

based on running applications.

### Model Training

The project uses:

* Random Forest Regressor
* Label Encoding for categorical context data
* Scikit-learn for training and prediction

Target Variable:

```text
Battery Drain Rate
```

### Prediction

The trained model predicts:

* Expected battery drain rate
* Estimated remaining battery life

for different workload scenarios.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* psutil
* Tkinter
* Joblib

## Installation

Clone the repository:

```bash
git clone https://github.com/hannishreddi/battery-widget.git
cd battery-widget
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn psutil joblib
```

## Usage

### Step 1: Collect Data

Run the data collection script:

```bash
python collector.py
```

This generates battery usage data inside:

```text
data.csv
```

### Step 2: Train Model

```bash
python train_model.py
```

This creates:

```text
model.pkl
encoder.pkl
```

### Step 3: Launch Widget

```bash
python widget.py
```

The widget will display:

* Current battery percentage
* Predicted battery drain
* Estimated battery life for different usage contexts

## Sample Output

```text
Battery: 78%

Coding: 145.2 min
Browsing: 132.8 min
Gaming: 94.1 min
Idle: 220.4 min
```

## Future Improvements

* Larger dataset collection
* Additional machine learning models
* Feature importance analysis
* Battery health prediction
* Windows executable packaging
* Improved UI/UX
* Deep learning experimentation

## Author

**Anumulla Hannish Reddi**

* GitHub: https://github.com/hannishreddi
* LinkedIn: https://www.linkedin.com/in/hannish-reddi-55024b266/

---

*Developed as a Fundamentals of Machine Learning project to explore data collection, feature engineering, supervised learning, and real-time ML deployment.*
