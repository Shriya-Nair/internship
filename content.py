from sklearn.decomposition import NMF
import numpy as np

# Assuming we have user-item interaction data in a matrix
# Rows represent users, columns represent items, and values represent interactions (e.g., ratings)
# Replace this with your actual data
user_item_matrix = np.array([[1, 0, 2, 0], [0, 3, 0, 4], [5, 0, 0, 6]])

# Initialize and fit the NMF model
model = NMF(n_components=2, init='random', random_state=42)
model.fit(user_item_matrix)

# Get user and item latent factors
user_factors = model.transform(user_item_matrix)
item_factors = model.components_

# Recommend items for a user (e.g., user_id = 0)
user_id = 0
user_item_scores = np.dot(user_factors[user_id], item_factors)
recommended_items = np.argsort(user_item_scores)[::-1]

print("Recommended items for user", user_id, ":", recommended_items)
