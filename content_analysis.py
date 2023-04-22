import nltk
import pandas as pd
#import textract
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag
import chardet

# Download the necessary resources
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('vader_lexicon')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

# Load the article text from a file
input_file = 'dfs_test.txt'

# Detect the file encoding and read its content
with open(input_file, 'rb') as file:
    raw_data = file.read()
    detected_encoding = chardet.detect(raw_data)['encoding']
    article_text = raw_data.decode(detected_encoding, errors='replace')

# Tokenize the article into sentences and words
sentences = sent_tokenize(article_text)
words = word_tokenize(article_text)

# Use Named Entity Recognition to extract names and locations
tagged_words = pos_tag(words)
named_entities_tree = ne_chunk(tagged_words)
named_entities = []
for t in named_entities_tree.subtrees():
    if t.label() in ['PERSON', 'GPE']:
        entity_name = ' '.join(c[0] for c in t.leaves())
        entity_type = 1 if t.label() == 'PERSON' else 0
        named_entities.append((entity_name, entity_type))

# Perform sentiment analysis on sentences containing each unique entity
sia = SentimentIntensityAnalyzer()
sentiment_data = []
for entity, entity_type in set(named_entities):
    entity_sentences = [sent for sent in sentences if entity in sent]
    if entity_sentences:
        sentiment = sum(sia.polarity_scores(sent)['compound'] for sent in entity_sentences) / len(entity_sentences)
    else:
        sentiment = 0  # or any other default value
    sentiment_data.append((entity, sentiment, entity_type))

# Sort the scores from highest to lowest
sorted_sentiment_data = sorted(sentiment_data, key=lambda x: x[1], reverse=True)

# Function to merge single-named entities with the same sentiment score
def merge_single_named_entities(sentiment_data):
    merged_data = []
    single_named_entities = {entity: (score, entity_type) for entity, score, entity_type in sentiment_data if len(entity.split()) == 1}

    while single_named_entities:
        entity, (score, entity_type) = single_named_entities.popitem()
        matched_entity = None
        for other_entity, (other_score, other_entity_type) in single_named_entities.items():
            if score == other_score and entity_type == other_entity_type:
                matched_entity = other_entity
                break

        if matched_entity:
            full_name = f"{entity} {matched_entity}"
            merged_data.append((full_name, score, entity_type))
            del single_named_entities[matched_entity]
        else:
            merged_data.append((entity, score, entity_type))

    # Add back the non-single-named entities
    merged_data.extend([(entity, score, entity_type) for entity, score, entity_type in sentiment_data if len(entity.split()) > 1])

    return merged_data

# Merge single-named entities with the same sentiment score
merged_sentiment_data = merge_single_named_entities(sorted_sentiment_data)

# Create a properly formatted DataFrame
df = pd.DataFrame(merged_sentiment_data, columns=['Entity', 'Sentiment','IsPerson']).sort_values('Sentiment', ascending=False)
df = df[df.IsPerson == 1]
df.drop('IsPerson', axis=1, inplace=True)
df.to_csv('dfs_test3.csv', index=False)
print("Sentiment Analysis Complete!")
