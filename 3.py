import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

def morphological_analysis(text):
    # Tokenize the input text into words
    words = nltk.word_tokenize(text)
    print(f"Original Words: {words}")

    # Initialize stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Perform stemming
    stemmed_words = [stemmer.stem(word) for word in words]
    print(f"Stemmed Words: {stemmed_words}")

    # Perform lemmatization
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    print(f"Lemmatized Words: {lemmatized_words}")

    # Perform lemmatization with parts of speech (default is noun)
    lemmatized_verbs = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in words]
    print(f"Lemmatized Verbs: {lemmatized_verbs}")


if __name__ == "__main__":
    # Input text for morphological analysis
    text = "The geese are flying and running quickly."
    print(f"Input Text: {text}\n")

    # Perform morphological analysis
    morphological_analysis(text)
