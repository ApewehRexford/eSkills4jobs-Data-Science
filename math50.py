# if they enter a value under 10,display the
# message "Too low " and ask them to try again
#     if they enter avalue above 20, display the
# message "Too high" and ask them to try again 
#     keep repeating this until they enter a value 
#     that is between 10 and 20 and then display the message "thank you"

user_input = int(input("Enter a number  b/n 10 and 20: "))

while (user_input < 10) or (user_input > 20):
    if user_input < 10:
        print("Too low")
        #user_input = int(input("Enter the guess again: "))
    if user_input > 20:
        print("Too high")
        #user_input = int(input("Enter the guess again: "))
    user_input = int(input("Enter the guess again: ")) 
print("Thank you")        