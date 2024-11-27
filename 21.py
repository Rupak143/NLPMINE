import spacy

# Load SpaCy English language model
nlp = spacy.load("en_core_web_sm")

def extract_noun_phrases(text):
    # Process the input text
    doc = nlp(text)
    
    # Extract noun phrases
    print("Extracted Noun Phrases and Their Meanings:")
    for np in doc.noun_chunks:
        print(f"- Noun Phrase: {np.text}")
        print(f"  Root Token: {np.root.text} ({np.root.pos_})")
        print(f"  Dependencies: {np.root.dep_}")
        print("  Full Phrase Meaning:", explain_noun_phrase(np))
        print()

def explain_noun_phrase(np):
    """
    Constructs a basic explanation of a noun phrase based on its components.
    """
    head_word = np.root.text
    modifiers = [token.text for token in np if token != np.root]
    meaning = f"The phrase is centered around '{head_word}', modified by '{', '.join(modifiers)}'" if modifiers else f"The phrase refers to '{head_word}' alone."
    return meaning

if __name__ == "__main__":
    # Input text for semantic analysis
    text = """
    The quick brown fox jumped over the lazy dog.
    A group of students visited the new museum in the city.
    """
    
    print(f"Input Text:\n{text}\n")
    
    # Perform noun phrase extraction and semantic analysis
    extract_noun_phrases(text)
