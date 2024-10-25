# Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what
# case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this
# second question, display the answer “It is too windy for an umbrella”, otherwise display the
# message “Take an umbrella”. If they did not answer yes to the first question, display the
# answer “Enjoy your day”.

#asking the user whether it is raining and converting to lower case
print("Enter [yes] or [no]  to the following questions")
user = input("Is it raining? " .lower())
#if yes, asking whether it is windy
if (user == "yes"):
    user2 = input("Is it windy? ")
    if (user2 == "yes" ):
        print("It is too windy for an umbrella ")
    else:
        print("Take an umbrella")
   
else:
    print("enjoy your day")

