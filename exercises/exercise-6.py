# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Type the 3 digit abbreviation for the month: ")
day = int(input("Type the number of the date: "))

if (((month == 'Jan') and (day > 0) and (day < 32)) or ((month == 'Feb') and (day < 29) and (day > 0)) or ((month == 'Dec') and (day >= 21) and (day <= 31)) or ((month == 'Mar') and (day <= 19) and (day > 0))):
    season = 'winter'
elif (((month == 'Apr') and (day > 0) and (day < 30)) or ((month == 'May') and (day > 0) and (day < 32)) or ((month == 'Mar') and (day > 20) and (day < 32)) or ((month == 'Jun') and (day > 20) and (day <= 30))):
    season = 'spring'
elif (((month == 'Jul') and (day > 0) and (day <= 31)) or ((month == 'Aug') and (day > 0) and (day <= 31)) or ((month == 'Jun') and (day >= 21) and (day <= 31)) or ((month == 'Sep') and (day >= 21) and (day <= 30))):
    season = 'summer'
elif (((month == 'Oct') and (day > 0) and (day <= 31)) or ((month == 'Nov') and (day > 0) and (day <= 30)) or ((month == 'Sep') and (day >= 21) and (day <= 30)) or ((month == 'Dec') and (day > 0) and (day <= 21))):
    season = 'fall'
else:
    season = 'invalid'

print(f"{month} {day} is the {season} season.")
