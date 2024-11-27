import nltk
from nltk import CFG, PCFG
from nltk.parse import ViterbiParser
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | V NP PP [0.3]
    V -> 'saw' [1.0]
    NP -> 'John' [0.5] | 'Mary' [0.5]
    PP -> P NP [1.0]
    P -> 'with' [1.0]
""")
parser = ViterbiParser(grammar)
sentence = ['John', 'saw', 'Mary']
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
