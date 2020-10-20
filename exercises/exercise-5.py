# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

number_terms = int(input("How many terms of the Fibonacci sequnce: "))

num1 = 0
num2 = 1
count = 0

if number_terms <= 0:
    print("You must enter a positive integer")
elif number_terms == 1:
    print(f"Fibonacci sequence up to {number_terms}: ")
    print(num1)
else:
    print("Fibonacci sequence:")
    while count < number_terms:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1
