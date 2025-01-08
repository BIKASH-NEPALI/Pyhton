#Write a program to detect spam comments:
s1="Make a lot of Money"
s2="buy now"
s3="suscribe this"
s4="click this"
# in key: if the word is present in sentence the it's 'true' otherwise 'false'
message=input("Enter your comment:")
if(s1 in message or s2 in message or s3 in message or s4 in message):
    print("This is a spam")
else:
    print("this is a comment")