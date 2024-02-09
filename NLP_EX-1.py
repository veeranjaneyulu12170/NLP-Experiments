#//printing words from sentence
import spacy
nlp=spacy.load('en_core_web_sm')

text = "SpaCy is an amazing tool for natural language processing."

doc = nlp(text)

for token in doc:
    print(f"Token: {token.text}")

