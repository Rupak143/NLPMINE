import nltk


def pos_tagging(text):
    """
    Perform part-of-speech tagging on the given text.
    """
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    print(f"Tokenized Words: {words}")
    
    # Perform POS tagging
    tagged_words = nltk.pos_tag(words)
    print("\nPart-of-Speech Tagged Words:")
    for word, tag in tagged_words:
        print(f"{word}: {tag}")

if __name__ == "__main__":
    # Input text
    text = "The quick brown fox jumps over the lazy dog."
    print(f"Input Text: {text}\n")
    
    # Perform POS tagging
    pos_tagging(text)
