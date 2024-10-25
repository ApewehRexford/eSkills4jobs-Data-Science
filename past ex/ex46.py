#ask the user to enter a number.Keep asking until they enter a value over
#5 and then displayy the message "The last number you entered was a [number]" and stop the program


user_num = int(input("Enter a number: "))
while (user_num <= 5 ):
    #loop control
    user_num = int(input("Enter another number: "))#while user is inputting a number less than 5, it would continue 
    #asking until its greater than 5
##this prints if the user inputs a number greater than 5, then after it outputs the last number you entered   
print("The last number you entered was ", user_num)
print("---------------------------------------------")
print(f"The last number entered was {user_num}")