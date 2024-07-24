# Sentiment Analysis on YouTube Comments

This project aims to analyze and categorize the sentiment of YouTube comments using Natural Language Processing (NLP) techniques. The provided scripts help preprocess the comments, categorize them based on sentiment, and build a machine learning model to predict the sentiment.

## Project Structure

1. **comment_dataset.py**:
    - Contains functions for preprocessing text data.
    - Replaces unwanted characters and transforms text to lowercase for uniformity.

2. **data.py**:
    - Loads the YouTube comments dataset.
    - Categorizes comments based on predefined positive and negative keywords.

3. **main.py**:
    - Utilizes sklearn to build a sentiment analysis model.
    - Preprocesses the data, trains a Naive Bayes classifier, and evaluates its performance.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/suman1406/Youtube_Comments_Sentiment_Analysis.git
    ```

2. **Install dependencies**:
    ```bash
    pip install pandas scikit-learn google-api-python-client
    ```

3. **Run the scripts**:
    - Ensure you have the required dataset (`youtube_comments.csv`) in the project directory.
    - Execute `main.py` to preprocess data, train the model, and evaluate its performance.

## Usage

- Preprocess comments using `preprocess_text` function from `comment_dataset.py`.
- Categorize comments using `categorize_sentiment` function in `data.py`.
- Train and evaluate the sentiment analysis model using the script in `main.py`.