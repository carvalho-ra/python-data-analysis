# 🚀 Customer Churn Exploratory Data Analysis

## 📋 Description

This project performs exploratory data analysis (EDA) in Python to identify patterns related to customer churn and propose strategies to reduce cancellations. It uses a fictitious dataset and libraries such as Pandas and Plotly for data manipulation and visualization.

## 🛠️ Technologies Used

- Python 3  
- Pandas — data manipulation and cleaning  
- Plotly — interactive and static visualizations  
- Kaleido — exporting Plotly charts as images  

## ⚙️ How It Works

- 📥 Loads customer dataset from a CSV file.  
- 🧹 Cleans and preprocesses data by removing irrelevant columns and handling missing values.  
- 📊 Generates color-coded histograms to visualize the relationship between features and customer churn.  
- 🔍 Applies filtering conditions to simulate scenarios aimed at reducing churn.  
- 🖼️ Saves charts as PNG images in `pre-resolution` and `post-resolution` directories for before/after analysis.

## ✅ Setup Instructions

### 📌 Prerequisites

- Python 3 installed on your system

### 🧱 Environment Setup

1. Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate    # Linux / MacOS
venv\Scripts\activate       # Windows
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Analysis

Run the main Python script or open the Jupyter Notebook to execute the analysis and generate charts:

```bash
python main.py
```

### ⚠️ Important Notes

- The project generates PNG images of graphs in the pre-resolution and post-resolution folders.
- For best interactive experience, use Jupyter Notebook.
- Kaleido is required to export Plotly charts as images.