import random
# pi = (22/7)
# # print(math(pi)) using this would bring an error because we havent imported math
# print(pi)
# #using import math makes it such that you dont have to be putting in forumulars
# import math
# import random
# print(math.sqrt(pi))

# #using the random
# pick_an_item = random.choice(['red', 'green' , 'blue'])
# print(pick_an_item)

##generate a random int number
##random with a sequence /range
rand_number = random.randint(0,9)#using randint to generate random integers(from rand for random and int for interger)
print(rand_number)

#git/ github / file system terminal
#generating without giving a range
num = random.random()#we use random. for the case were we dont give a range
print(num)