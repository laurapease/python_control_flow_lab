# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


l = input("Enter the character: ")
if l.lower() in ('a', 'e', 'i', 'o', 'u'):
    print('This is a vowel.')
elif l.upper() in ('A', 'E', 'I', 'O', 'U'):
    print('This is a vowel.')  
elif l.lower() in ('y'):
    print('This is sometimes a vowel and sometimes a consonant')
elif l.upper() in ('Y'):
    print('This is sometimes a vowel and sometimes a consonant')  
else: 
    print('This is a consonant')

