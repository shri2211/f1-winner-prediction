
# Formula 1 Grand Prix Winner Prediction

## 📌 Project Overview
This project predicts **Formula 1 race winners** using historical data from **1950–2024**, sourced from Kaggle.  
The predictive model analyzes historical qualifying positions, race results, and constructor performance to forecast race outcomes.

The goal of this project is to provide **actionable insights** through data-driven analysis and an **interactive dashboard**, where users can:
- Select a race track and view predictions for the top 3 finishers
- Compare qualifying positions vs. fastest lap times
- See winning probabilities for current drivers and constructors

---

## 🚀 Features
- **Winner Prediction** – Forecasts the most likely driver to win a selected race
- **Top 3 Finishers** – Displays the top three predicted finishers with key stats
- **Qualifying vs. Fastest Lap Analysis** – Interactive scatter plot for performance insights
- **Interactive Dashboard** – Built with Streamlit for easy access and visualization

---

## 🛠️ Tech Stack
| Tool / Library     | Purpose                        |
|--------------------|--------------------------------|
| **Python**         | Core programming language      |
| **Pandas**         | Data cleaning and manipulation |
| **NumPy**          | Numerical operations           |
| **Matplotlib**     | Visualizations and plots       |
| **Scikit-learn**   | Machine learning (Random Forest) |
| **Streamlit**      | Interactive dashboard & deployment |

---

## 📂 Project Structure
```
project-folder/
│
├── .gitignore              # Files/folders to ignore in Git
├── README.md               # Project documentation
├── requirements.txt        # Dependencies for Streamlit Cloud
│
├── f1_data_cleaning.ipynb  # Notebook for cleaning and preparing data
├── f1_prediction_model.ipynb # Notebook for training and testing the model
├── f1_cleaned_data.csv     # Cleaned dataset used for predictions
├── f1_simple_predictions.csv # Model prediction output
├── f1predictor.py          # Streamlit app
│
├── csv files/              # Raw Kaggle datasets
└── .ipynb_checkpoints/     # Jupyter auto-save files (ignored)
```

---

## ⚙️ Setup Instructions
Follow these steps to run the project locally or deploy to Streamlit Cloud.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shri2211/f1-winner-prediction.git
cd f1-winner-prediction
```

### 2️⃣ Install Dependencies
Install all required libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App Locally
```bash
streamlit run f1predictor.py
```
This will open the interactive dashboard in your browser.

---

## 🌍 Deployment (Streamlit Cloud)
The project is deployed using **Streamlit Cloud**:
1. Push your project to a public GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in.
3. Create a **New App** → select your GitHub repo.
4. Set **Main file path** to:
   ```
   f1predictor.py
   ```
5. Deploy — Streamlit will generate a shareable public URL.

---

## 📊 Data
- **Source:** [Formula 1 World Championship Dataset by Rohan Rao](https://www.kaggle.com/rohanrao/formula-1-world-championship-1950-2020)
- **Contents:** Includes race results, drivers, constructors, circuits, qualifying, and status data.

---

## 🧾 Business Context
This project demonstrates skills in **business analytics** and **AI-driven decision-making**:
- Uses historical performance metrics to predict race outcomes
- Builds interactive visualizations for team strategy analysis
- Showcases predictive modeling for real-world sports data

---

## 🔗 Live App
Access the live project here:  
[**Formula 1 Winner Predictor**](https://f1-winner-prediction-model.streamlit.app/)

---

## ✍️ Author
**Shrivardhan K. Gowrish**  
Business Analytics & AI Student | Aspiring Data Analyst
