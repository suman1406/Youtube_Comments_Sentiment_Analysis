import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

from comment_dataset import get_comments, get_video_id, preprocess_text

comments_df = pd.read_csv('youtube_comments.csv')
comments_df['comment'] = comments_df['comment'].apply(preprocess_text)

comments_df['label'] = ['positive'] * len(comments_df)

X_train, X_test, y_train, y_test = train_test_split(comments_df['comment'], comments_df['label'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

y_pred = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

def predict_sentiment(comment):
    comment = preprocess_text(comment)
    vectorized_comment = vectorizer.transform([comment])
    prediction = model.predict(vectorized_comment)
    return prediction[0]

while True:
    video_url = input("Enter the YouTube video URL (or type 'exit' to quit): ")
    if video_url.lower() == 'exit':
        break

    video_id = get_video_id(video_url)

    if video_id:
        comments = get_comments(video_id)
        print(f"Fetched {len(comments)} comments from the video.")

        comments_df = pd.DataFrame(comments, columns=['comment'])
        comments_df.to_csv('youtube_comments.csv', index=False)
        print("Comments saved to youtube_comments.csv")

        for comment in comments:
            sentiment = predict_sentiment(comment)
            print(f"Comment: {comment}")
            print(f"Predicted Sentiment: {sentiment}\n")
    else:
        print("Invalid YouTube URL.")
