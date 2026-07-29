"""
preprocessing.py

This module performs basic text preprocessing.
"""

import pandas as pd


def clean_text(text):
    """
    Basic text cleaning.
    """
    if pd.isna(text):
        return ""

    text = text.lower().strip()
    return text


if __name__ == "__main__":
    print("Preprocessing Module")