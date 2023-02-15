# Print Hello User!
print("Hello user!")

# Take in User Input
userName = input("What is your name?")

# Respond Back with User Input
print("Hello "+ userName)

# Take in the User Favorite Number
favNumber = int(input("What is your favorite number?"))

# Respond Back with a statement based on your favorite number
if favNumber > 5:
    print("Your favorite number is greater than mine.")
elif favNumber < 5:
    print("Your favorite number is less than mine.")
else:
    print("Your favorite color is the same as mine!")   