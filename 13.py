import nltk
from nltk import CFG, ChartParser
from nltk.tree import Tree
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP | V
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'ball' | 'park'
    V -> 'chases' | 'sees' | 'plays'
    P -> 'in' | 'with'
""")
parser = ChartParser(grammar)

def generate_parse_tree(sentence):
    print(f"Parsing the sentence: {' '.join(sentence)}\n")
    try:
        trees = list(parser.parse(sentence))
        if not trees:
            print("No valid parse trees found.\n")
        else:
            for i, tree in enumerate(trees, 1):
                print(f"Parse Tree {i}:")
                print(tree)
                tree.pretty_print()
                print()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sentences = [
        "the dog chases the cat",
        "the dog plays with the ball",
        "a cat sees the dog in the park",
    ]
    for sentence in sentences:
        tokens = sentence.split()
        generate_parse_tree(tokens)
