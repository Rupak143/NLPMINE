import re
from nltk import word_tokenize

def rule_based_pos_tagger(sentence):
    """
    A simple rule-based POS tagger using regular expressions.
    """
    # Define tagging rules as (pattern, tag)
    rules = [
        (r".*ing$", "VBG"),  # Gerunds (e.g., running, eating)
        (r".*ed$", "VBD"),   # Past tense verbs (e.g., jumped, played)
        (r".*s$", "NNS"),    # Plural nouns (e.g., cats, dogs)
        (r".*ly$", "RB"),    # Adverbs (e.g., quickly, slowly)
        (r".*able$", "JJ"),  # Adjectives (e.g., adorable, capable)
        (r"^[A-Z].*", "NNP"),# Proper nouns (e.g., John, New York)
        (r"\d+", "CD"),      # Numbers (e.g., 123, 2023)
        (r".*", "NN")        # Default: noun (e.g., table, book)
    ]
    
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    
    # Apply rules to each word
    tagged_sentence = []
    for word in words:
        for pattern, tag in rules:
            if re.fullmatch(pattern, word):
                tagged_sentence.append((word, tag))
                break  # Exit the loop after the first match
    
    return tagged_sentence

if __name__ == "__main__":
    # Input sentence
    sentence = "John quickly played the adorable game with 3 dogs."
    print(f"Input Sentence: {sentence}\n")
    
    # Perform rule-based POS tagging
    tagged_sentence = rule_based_pos_tagger(sentence)
    
    # Display the tagged sentence
    print("Tagged Sentence:")
    for word, tag in tagged_sentence:
        print(f"{word}: {tag}")
