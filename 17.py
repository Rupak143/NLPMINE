from nltk.corpus import wordnet as wn
import nltk

def explore_wordnet(word):
    synsets = wn.synsets(word)
    print(f"\nWord: {word}")
    print(f"Number of Synsets: {len(synsets)}")

    for i, synset in enumerate(synsets):
        print(f"\nSynset {i + 1}: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print(f"Lemmas: {[lemma.name() for lemma in synset.lemmas()]}")

    synonyms = set()
    antonyms = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())

    print(f"\nSynonyms: {synonyms}")
    print(f"Antonyms: {antonyms}")

word_to_explore = "happy"

explore_wordnet(word_to_explore)
