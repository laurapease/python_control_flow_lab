# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

human_age = int(input("Please enter your dog's age in human years: "))

if human_age < 0:
    print("Age must be greater than zero")
    exit()
elif human_age <= 2:
    dog_age = human_age * 10
else:
    dog_age = 20 + (human_age - 2)*4

print(f"The dog's age is {dog_age} in dog years")
