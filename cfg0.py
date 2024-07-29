import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
        
AP -> A | AP                              
NP -> N | D NP | AP NP | N PP
PP -> P NP                                               
VP -> V | V NP | V NP PP

A -> "big" | "blue" | "small" | "wide"
D -> "the" | "a" | "an"     
N -> "she" | "city" | "car" | "dog" | "binoculars"
P -> "on" | "over" | "before" | "after" |"with"
V -> "walked" | "run" | "saw" | "jump"
      
""")

parser = nltk.ChartParser(grammar)

sentence = input("Sentence: ").split()

try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
except ValueError:
    print("No parse tree possible")