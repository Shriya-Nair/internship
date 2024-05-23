import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Example abusive and non-abusive texts
texts = [
    "I hate you! Go away!",
    "This is a great community. I love it!",
    "You are an idiot and should be banned.",
    "Thank you for your helpful response."
]
labels = [1, 0, 1, 0]  # 1 for abusive, 0 for non-abusive

# Tokenize texts
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
max_length = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_length)

# Build and compile the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(padded_sequences, labels, epochs=10, verbose=1)

# Predict on new texts
new_texts = ["You are so dumb.", "Thanks for the help!"]
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_padded_sequences = pad_sequences(new_sequences, maxlen=max_length)
predictions = model.predict(new_padded_sequences)

for i, text in enumerate(new_texts):
    print(f"Text: {text} - Predicted label: {'Abusive' if predictions[i] > 0.5 else 'Non-abusive'}")
