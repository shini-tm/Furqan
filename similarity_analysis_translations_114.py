from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import gensim.downloader as api

# Sample translations
translations = ['the God of humankind,', 'the God of mankind,', 'I am jack,', 'the God of mankind,']

# Pre-trained Word2Vec model (you need to download and load a model here)
word2vec_model = api.load("word2vec-google-news-300", return_path=True)

# Function to convert a sentence to a vector using Word2Vec
def sentence_to_vector(sentence, model):
    words = sentence.lower().split()
    vector = []
    for word in words:
        print("THE WORD IS:", word)
        try:
            vector.append(model[word])
        except KeyError:
            # Handle cases where the word is not in the model's vocabulary
            print("'",word, "' not in model")
            pass
    return sum(vector) / len(vector) if vector else [0.0] * 300  # Use vector dimension of your model

# Calculate similarity scores
similarity_scores = []

for i, translation_i in enumerate(translations):
    scores_i = []
    vector_i = sentence_to_vector(translation_i, word2vec_model)

    for j, translation_j in enumerate(translations):
        vector_j = sentence_to_vector(translation_j, word2vec_model)
        score = cosine_similarity([vector_i], [vector_j])[0][0]
        scores_i.append(score)

    similarity_scores.append(scores_i)

# Print the similarity scores
for i, translation in enumerate(translations):
    print(f"Translation {i + 1}:")
    for j, score in enumerate(similarity_scores[i]):
        print(f"Similarity to Translation {j + 1}: {score:.2f}")
    print()
