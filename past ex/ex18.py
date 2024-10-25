# Ask the user to enter a number. If it is under 10, display the message “Too low”, if their
# number is between 10 and 20, display “Correct”, otherwise display “Too high”


user_num = int(input("Enter a number: "))
if (user_num < 10):
    print("Too low")
elif ((user_num >=10 ) and (user_num <= 20)):
    print("correct")
else:
    print("Too high")        