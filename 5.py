from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# List of words to stem
words = [
    "running", "runner", "ran", "easily", "flying", 
    "flies", "happiness", "troubling", "troubles", "trouble"
]

# Perform stemming
print("Word Stemming using Porter Stemmer:")
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"{word} → {stemmed_word}")
