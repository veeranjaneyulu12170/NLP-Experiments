##Dividing Two sentences
nlp = spacy.load('en_core_web_sm')
sentence = "I like coffee, but I don't like tea."

doc = nlp(sentence)

split_sentences = []
current_sentence = []

for token in doc:
    if token.text.lower() in ['and', 'but', 'or', 'nor', 'for', 'so', 'yet']:
        split_sentences.append(' '.join(current_sentence))
        current_sentence = []
    else:
        current_sentence.append(token.text)

split_sentences.append(' '.join(current_sentence))


for i, sentence in enumerate(split_sentences):
    print(f"Sentence {i + 1}: {sentence}")
