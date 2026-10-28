name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_subject = input("Enter your favourite subject: ")


print(f"Hello {name}! You are {age} years old and your favourite subject is {fav_subject}.")

current_year = 2026
years_left = 30 - age
turning_30_year = current_year + years_left

print(f"You will turn 30 years old in the year {turning_30_year}.")