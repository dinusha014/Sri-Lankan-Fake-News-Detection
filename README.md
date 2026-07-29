# 🇱🇰 Sri Lankan Fake News Detection

## Project Overview

This project is developed as part of the **IT41043 – Intelligent Systems** module at **Horizon Campus**. The aim of this research is to develop a machine learning-based fake news detection system for the Sri Lankan context. The system focuses on classifying news articles and social media posts as **Real** or **Fake** using both traditional machine learning and transformer-based deep learning techniques.

The project compares **TF-IDF with Logistic Regression** as the baseline model and **Multilingual BERT (mBERT)** as the proposed model.

---

## Research Problem

The rapid spread of fake news on social media has become a major challenge in Sri Lanka. False information related to politics, health, religion, and social issues spreads quickly and can mislead the public. Existing fake news detection systems mainly focus on English-language content and often perform poorly when handling Sinhala and Sinhala-English code-mixed text.

This research aims to address this limitation by developing a multilingual fake news detection model suitable for the Sri Lankan social media environment.

---

## Research Objectives

### Main Objective

To evaluate the effectiveness of a machine learning-based fake news detection model in reducing social misinformation among Sri Lankan social media users aged 18–35.

### Specific Objectives

- Collect a multilingual Sri Lankan fake news dataset.
- Preprocess textual data for machine learning.
- Develop a baseline model using TF-IDF and Logistic Regression.
- Develop a transformer-based model using Multilingual BERT (mBERT).
- Compare the performance of both models using standard evaluation metrics.

---

## Dataset

The planned dataset will contain approximately **2,000** text samples collected from publicly available Sri Lankan news websites and fact-checking sources.

### Dataset Distribution

| Category | Count |
|----------|------:|
| Real News | 1000 |
| Fake News | 1000 |
| Total | 2000 |

### Languages

- Sinhala
- English
- Sinhala-English Code-Mixed

### Categories

- Politics
- Economy
- Health
- Religion
- Ethnic and Social Issues
- Natural Disasters
- General Rumours

---

## Proposed Methodology

The project follows these main stages:

1. Data Collection
2. Data Preprocessing
3. Text Cleaning
4. Feature Extraction
5. Baseline Model (TF-IDF + Logistic Regression)
6. Proposed Model (Multilingual BERT)
7. Model Evaluation
8. Performance Comparison

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

---

## Project Structure

```text
Sri-Lankan-Fake-News-Detection/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── src/
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── baseline_model.py
│   ├── proposed_model.py
│   ├── evaluation.py
│   └── __init__.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── diagrams/
│   ├── system_architecture.drawio
│   └── system_architecture.png
│
├── references/
│   └── reference_list.md
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── .env.example
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Hugging Face Transformers
- PyTorch
- NLTK
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Sri-Lankan-Fake-News-Detection.git
```

Navigate to the project directory:

```bash
cd Sri-Lankan-Fake-News-Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Current Progress

- Literature review completed.
- Research proposal completed.
- Methodology designed.
- Dataset planning completed.
- GitHub repository created.
- Initial project structure completed.
- Source code modules created.
- Baseline model selected.
- System architecture designed.

---

## Future Work

- Collect the complete dataset.
- Perform data preprocessing.
- Train the baseline model.
- Train the Multilingual BERT model.
- Evaluate model performance.
- Compare experimental results.
- Document findings and prepare the final report.

---

## Authors

**U.K.R.R.P. Ayuwardhana**  
**W.H.C.D.J. Karunanayaka**

**BSc (Hons) in Information Technology**  
Faculty of Information Technology  
Horizon Campus

**Module:** IT41043 – Intelligent Systems

---

## License

This project is developed for academic and educational purposes as part of the IT41043 – Intelligent Systems module at Horizon Campus.