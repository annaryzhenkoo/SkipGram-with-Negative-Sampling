import numpy as np

def get_top_n_similar_words(
    model,
    word: str,
    word2id: dict,
    id2word: dict,
    n: int = 10,
    use_central: bool = True
):

    if word not in word2id:
        raise ValueError(f"Word '{word}' not in vocabulary")

    word_id = word2id[word]

    if use_central:
        embeddings = model.V
    else:
        embeddings = model.U

    norms = np.linalg.norm(embeddings, axis=1, keepdims=True) + 1e-10
    normalized = embeddings / norms

    query_vec = normalized[word_id]
    similarities = normalized @ query_vec


    similarities[word_id] = -np.inf

    top_ids = np.argsort(similarities)[-n:][::-1]

    results = [(id2word[i], float(similarities[i])) for i in top_ids]

    return results