import nltk
from nltk.tokenize import word_tokenize

def initial_tagging(words):
    """
    Assigns an initial tag to each word using simple rules.
    """
    tags = []
    for word in words:
        if word.istitle():  # Starts with a capital letter
            tags.append((word, "NNP"))  # Proper noun
        elif word.isdigit():  # Is a number
            tags.append((word, "CD"))  # Cardinal number
        elif word.endswith("ing"):  # Ends with "ing"
            tags.append((word, "VBG"))  # Verb (gerund)
        elif word.endswith("ed"):  # Ends with "ed"
            tags.append((word, "VBD"))  # Verb (past tense)
        else:
            tags.append((word, "NN"))  # Default to noun
    return tags

def apply_transformation_rules(tagged_words):
    """
    Applies transformation rules to refine the initial tags.
    """
    rules = [
        # If the word is 'is', change its tag to VBZ (Verb, 3rd person singular present)
        (lambda word, tag: word.lower() == "is" and tag == "NN", "VBZ"),
        
        # If the word ends with "ly", change its tag to RB (Adverb)
        (lambda word, tag: word.endswith("ly") and tag == "NN", "RB"),
    ]

    transformed_tags = []
    for word, tag in tagged_words:
        transformed_tag = tag
        for condition, new_tag in rules:
            if condition(word, tag):
                transformed_tag = new_tag
                break
        transformed_tags.append((word, transformed_tag))
    return transformed_tags

if __name__ == "__main__":
    # Input sentence
    sentence = "The dog is happily playing in the garden."
    print(f"Input Sentence: {sentence}\n")

    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Step 1: Initial tagging
    initial_tags = initial_tagging(words)
    print("Initial Tags:")
    for word, tag in initial_tags:
        print(f"{word}: {tag}")

    # Step 2: Apply transformation rules
    refined_tags = apply_transformation_rules(initial_tags)
    print("\nRefined Tags:")
    for word, tag in refined_tags:
        print(f"{word}: {tag}")
