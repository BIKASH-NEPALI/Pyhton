''' Create an empty dictionary. Allow 4 friend to enter
their favourite languages as value and use keys as their names.
Assume that the names are unique'''
dictionary={}
name=input("Enter you name:")
language=input("enter your fav language")
dictionary.update({name:language})
name=input("Enter you name:")
language=input("enter your fav language")
dictionary.update({name:language})
name=input("Enter you name:")
language=input("enter your fav language")
dictionary.update({name:language})
name=input("Enter you name:")
language=input("enter your fav language")
dictionary.update({name:language})
print(dictionary)
# if two names are same then language will be update in same name
# if two language if will same then value will same , (indentifier)key is differ