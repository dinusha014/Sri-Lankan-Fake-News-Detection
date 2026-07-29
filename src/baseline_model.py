"""
baseline_model.py

Baseline model using TF-IDF and Logistic Regression.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def create_baseline_model():
    """
    Create the baseline machine learning model.
    """
    vectorizer = TfidfVectorizer()
    model = LogisticRegression()

    return vectorizer, model


if __name__ == "__main__":
    print("Baseline Model Module")