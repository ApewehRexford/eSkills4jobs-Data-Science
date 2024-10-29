##create an empty class register
class_reg = []

reg_count = int(input("Enter the number of students to register: "))
##25 participants

for each_user in range(1, reg_count + 1):
    ##ask for the users fullname
    user_input = input("Enter your fullname: ")
    print("Thank you, Next person!")
    print("----------------------------")
    
    ##
    class_reg.append(user_input)
##display the class register
print(class_reg)    
