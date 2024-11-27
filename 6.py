import random
from collections import defaultdict

def generate_bigrams(text):
    """
    Create bigrams from the given text and their frequencies.
    """
    tokens = text.split()  # Tokenize the text into words
    bigrams = list(zip(tokens[:-1], tokens[1:]))
    bigram_freq = defaultdict(list)
    
    # Build bigram frequency dictionary
    for w1, w2 in bigrams:
        bigram_freq[w1].append(w2)
    
    return bigram_freq

def generate_text(bigram_freq, start_word, num_words):
    """
    Generate text using the bigram model.
    """
    current_word = start_word
    output = [current_word]
    
    for _ in range(num_words - 1):
        if current_word in bigram_freq and bigram_freq[current_word]:
            next_word = random.choice(bigram_freq[current_word])
            output.append(next_word)
            current_word = next_word
        else:
            break
    
    return ' '.join(output)

if __name__ == "__main__":
    # Input text
    input_text = (
        "This is a simple example of a bigram model. "
        "A bigram model generates text based on word pairs. "
        "Word pairs can predict the next word."
    )
    
    # Generate the bigram model
    bigram_freq = generate_bigrams(input_text)
    
    # Starting word and number of words to generate
    start_word = "bigram"
    num_words = 10
    
    # Generate text
    generated_text = generate_text(bigram_freq, start_word, num_words)
    
    print("Generated Text:")
    print(generated_text)
