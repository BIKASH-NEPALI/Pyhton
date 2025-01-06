letter='''Dear <|Name|>,
you are selected!

<|date|>'''
apple=letter.replace("<|Name|>", "bikash").replace("<|date|>", "23 september!") #this is called chaingin like a loop.

print(apple)