doc="There were two kind of people"
pos=nlp(doc)

for post in  pos:
  print(f" {post.text} ==> {post.pos_}")
