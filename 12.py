import nltk
from nltk.parse.earleychart import EarleyChartParser
from nltk.grammar import CFG
grammar = CFG.fromstring("""
    S  -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N  -> 'cat' | 'dog'
    V  -> 'chased' | 'saw'
""")
parser = EarleyChartParser(grammar)
sentence = "the cat chased the dog".split()
for tree in parser.parse(sentence):
  print(tree)
  tree.pretty_print()
