import nltk
from nltk import CFG, ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det N PP
VP -> V NP | VP PP
PP -> P NP
Det -> 'a' | 'the'
N -> 'man' | 'dog' | 'cat'
V -> 'saw' | 'ate'
P -> 'with'
""")
def check_sentence(sentence):
    words = sentence.lower().split()
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(words):
        print(tree)
        return True
    return False
sentence = r"the man saw a dog with a cat"
if check_sentence(sentence):
  print("The sentence is grammatically correct.")
else:
  print("The sentence is not grammatically correct.")
