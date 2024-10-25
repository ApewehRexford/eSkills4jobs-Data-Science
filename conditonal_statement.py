# control statements in python
#control structures in python
# if 
# if-else
# if-elif-else


# Ask for two numbers. If the first one is larger than second number , display the second number then the 
# the first number otherwise show the first number first and second by the second number

## asking for two inputs and converting them to integer
# first_number = int(input("Enter your first number: "))

# second_number = int(input("Enter your second number: "))

##result = (first_number > second_number)

#conditional statement needed
#test for the condition and make a decision
# if (first_number > second_number):
#     print(second_number , first_number) 
# else:
#     print(first_number , second_number)    


#ask the user to enter a number that is under 20, if they enter a 
# number that is 20 or more, display the message 
#"Too high", otherwise display "Thank you"

#ask the user for their number
# num1 = int(input("Enter a number: "))
# #using conditional statement if the number is greater than 20 output too high
# if (num1 >= 20):
#     print("Too high")
# #using conditional statement else to output thank you if the number the number is less than 20    
# else:
#     print("Thank you")    


#14
#ask a uuser to enter a number between 10 and 20(inclusive).
#if they enter a number within this range, display the message
#"Thank you", other wise display the message "Incorrect Answer

# user_input = int(input("Enter a number b/n 10 and 20: "))
# if ((user_input >= 10) and (user_input <= 20)):
# # (10 <= user_input <= 20):
#     print("Thank you")
# else:
#     print("Incorrect Answer ")    


# ask the user to enter their favourite colour, 
# if they enter "red" , "RED" or "Red" display
# the message "I like red too ", other wise
# display the message "I dont like[colour]", I prefer red"

user_input = input("Enter your favourite colour: ")
#ask for the user input

if (user_input == "red" ) or (user_input == "RED") or (user_input == "Red"): 
    # display I like red/RED/Red if the user likes red or RED or Red
    print("I like" , user_input, "too")

else:
    #display I dont like [color ] if the user doesnt input red/RED/Red
    print("I dont like", user_input, ", I prefer red" )    
    

