# #Generate a seq of numbs b/n 1 and 10
# for each_number in range(1,10):
#     print("Each Number: => " , each_number)

# for a_number in range(1,11):
#     print("Number: " , a_number)    

# for a_number in range(2, 11 , 2): ##basically it is x + 2, where x = the starting number
#     print(a_number)    

# for neg in range(10, 0 , -2):
#     print(neg)
# class_reg = ["Apeweh" , "Jul" , "Rex" , "GEn"] #we use this box bracket for list
# for each_item in class_reg: 
#     print(each_item)


##ask the user to enter their name and then display their name three times
# user_name = input("Enter your name: ")
# for each_name in range(1,4):
#     # print("Your name is: " , user_name )
#     print(user_name)

#alter the program above so that it will ask the user to enter their username  and a number
# and then display their name that number of times

# user_name = input("Enter your name: ")
# user_num = int(input("Enter your number: "))
# for num_times in range(1, user_num + 1):
#     print("Your name is ", user_name)

#41 
#ask a user to enter their name and a number. If the  nuumber is less than 10, then
#display thier name that number of times, otherwise display the message "Too high"
#three times

user_name = input("Enter your name: ")
user_num =int(input("Enter a number: "))
if (user_num <= 10):
    for times in range(1, user_num + 1 ):
     print("Your name is : " , user_name)   
else:
   for number in range(1, 3 + 1):
    print("too high")
