import string
word = input("Enter the text which may be a palindrome: ")
translator = str.maketrans('','', string.punctuation)
nopunc = (word.translate(translator))
lowercase = (nopunc.lower())
finale = (lowercase.replace(" ",""))
reverse = (finale[::-1])
if finale == reverse:
	print("this is a palindrome :3")
else:
	print("this isn't a palindrome :C")
