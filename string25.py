#  025
#  Ask the user to enter their first name. If the length of their first name is under five characters, ask
#  them to enter their surname and join them together (without a space) and display the name in
#  upper case. If the length of the first name is five or more characters, display their first name in
#  lower case

user_fname = input("Enter your First name: ")
if len(user_fname) < 5:
 surname = input("Enter your surname: ")
 full_name = user_fname + surname
else:
 print(user_fname.lower())