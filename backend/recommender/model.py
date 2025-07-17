from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

tfidf_matrix = None
df_products = None

def train_model(df):
    """
    Fit TF-IDF on product descriptions and store the similarity matrix
    """
    global tfidf_matrix, df_products
    df_products = df

    # Initialize TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])

def get_recommendations(product_title, top_n=5):
    """
    Get top N recommended products similar to the given product_title.
    """
    # Find the index of the product
    idx = df_products[df_products['title'].str.lower() == product_title.lower()].index
    if len(idx) == 0:
        return []

    idx = idx[0]

    # Compute cosine similarity scores
    cosine_similarities = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Get indices of top N similar products
    similar_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]

    # Get product titles
    recommendations = df_products['title'].iloc[similar_indices].tolist()
    return recommendations



