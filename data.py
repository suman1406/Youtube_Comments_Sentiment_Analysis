import pandas as pd

comments_df = pd.read_csv('youtube_comments.csv')

def categorize_sentiment(comment):
    positive_keywords = ['good', 'great', 'best', 'love', 'excited', 'awesome', 'amazing', 'superhit', 'blockbuster', 'fantastic', 'waiting', 'nice', 'interesting', 'epic', 'well']
    negative_keywords = ['bad', 'worst', 'flop', 'waste', 'boring', 'terrible', 'bakwas', 'cringe']
    
    comment_lower = comment.lower()
    if any(word in comment_lower for word in positive_keywords):
        return 'positive'
    elif any(word in comment_lower for word in negative_keywords):
        return 'negative'
    else:
        return 'neutral'

comments_df['sentiment'] = comments_df['comment'].apply(categorize_sentiment)

comments_df.to_csv('youtube_comments_with_sentiments.csv', index=False)

print(comments_df.head())
