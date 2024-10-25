#  023
#  Ask the user to type in the first line of a nursery rhyme and display the length of the string.
#  Ask for a starting number and an ending number and then display just that section of the text
#  (remember Python starts counting from 0 and not 1)
# How I wonder what you are.
# Up above the world so high,
# Like a diamond in the sky



rhyme = input("Enter the first line of a nursery rhyme: ")
print(f"The length of the rhyme is {len(rhyme)}")
Nrhyme = int(input("A starting number: "))
Nrhyme2 = int(input("An ending number: "))
print(rhyme[Nrhyme:Nrhyme2])

































































































