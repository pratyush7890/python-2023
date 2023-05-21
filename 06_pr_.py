letter = '''Dear<|NAME|>,
 I am happy to regard you are selected my company( learn coding). Now you  can enjoy your days .
 You are selected!
 Thank you!
 Date : <|DATE|>

'''
name = input("Enter your name")
date = input("Enter your Date")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)