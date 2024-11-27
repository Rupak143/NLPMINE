import nltk
from nltk import word_tokenize
from collections import Counter, defaultdict
import random

from nltk.corpus import treebank

def train_pos_tagger(corpus):
    """
    Train a simple unigram POS tagger based on a given corpus.
    """
    # Flatten the corpus into a list of (word, tag) pairs
    word_tag_pairs = [(word.lower(), tag) for sent in corpus for word, tag in sent]
    
    # Count occurrences of each tag for each word
    word_tag_counts = defaultdict(Counter)
    for word, tag in word_tag_pairs:
        word_tag_counts[word][tag] += 1
    
    # Calculate probabilities (most frequent tag for each word)
    tag_probabilities = {}
    for word, tag_count in word_tag_counts.items():
        tag_probabilities[word] = max(tag_count, key=tag_count.get)
    
    return tag_probabilities

def stochastic_pos_tagger(sentence, tag_probabilities):
    """
    Use the trained POS tagger to tag a sentence.
    """
    words = word_tokenize(sentence)
    tagged_sentence = []
    for word in words:
        word_lower = word.lower()
        tag = tag_probabilities.get(word_lower, "NN")  # Default tag is NN (noun)
        tagged_sentence.append((word, tag))
    return tagged_sentence

if __name__ == "__main__":
    # Load the Treebank corpus
    corpus = treebank.tagged_sents(tagset="universal")
    
    # Train the POS tagger
    tag_probabilities = train_pos_tagger(corpus)
    
    # Input sentence for tagging
    sentence = "The quick brown fox jumps over the lazy dog."
    print(f"Input Sentence: {sentence}\n")
    
    # Perform stochastic POS tagging
    tagged_sentence = stochastic_pos_tagger(sentence, tag_probabilities)
    print("Tagged Sentence:")
    for word, tag in tagged_sentence:
        print(f"{word}: {tag}")
