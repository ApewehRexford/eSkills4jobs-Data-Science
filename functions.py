##global
def users_input():
    user_input1 = int(input("Enter  your first number: "))
    user_input2 = int(input("Enter  your second number: "))

    return user_input1, user_input2

##creating too add two number

#def addition (num1, num2):
    ##
#    result = num1 + num2
#    return result 
##call the addition function
#add = addition(3,4)
#rint(f"The sum of adding two numbers: {add}")

##subtracting two numbers
#def subtract(snum1, snum2):
##    result = snum1 - snum2
#    return result
#sub = subtract(4,5)
#print(f"The subtraction of two values is {sub}")

##multiplication of two numbers
#def multi(mnum1,mnum2):
#    result = mnum1 * mnum2
#    return result
#mnum1, mnum2 = users_input()
#mul = multi(mnum1,mnum2)
#print(f"The multiplication of the two values is {mul}")

#create a funtion that allows you 
#computing a sales commission,given the sales amount
#and the commission rate


def finance():
    sales_amount = float(input("Your sales amount:[Ghc] "))
    commission_rate = float(input("Your commission rate: "))
    return sales_amount, commission_rate

def sales_commission(sales,rate):
    result = sales * (rate/100)
    return result
sales, rate = finance()
my_commission = sales_commission(sales,rate)
print(f"The sales commission is [Ghc]{my_commission}")





