## REGX(printing digits from words)
nlp = spacy.load('en_core_web_sm')

sentence = "There are 3 apples and 5 oranges on the table."

doc = nlp(sentence)

numbers=[]
for token in doc:
    if token.is_digit:
        numbers.append(token.text)

print("Numbers in the sentence:", numbers)


