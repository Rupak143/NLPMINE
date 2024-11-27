import spacy
nlp = spacy.load("en_core_web_sm")
def perform_ner(text):
    doc = nlp(text)
    print("Named Entities, their labels, and explanations:")
    for entity in doc.ents:
        print(f"{entity.text:15} {entity.label_:10} {spacy.explain(entity.label_)}")
if __name__ == "__main__":
    text = """
    Apple Inc. is looking at buying U.K. startup for $1 billion. 
    Elon Musk, the CEO of Tesla, resides in Austin, Texas. 
    The next SpaceX launch is scheduled for January 2024.
    """
    print(f"Input Text:\n{text}\n")
    perform_ner(text)
