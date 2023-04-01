# Variables

hours = 30
rate = 15
pay = hours * rate
print(rate)

#Input in python

name = input("Who are you? ")
print("Welcome " + name)

#Age difference between Ali and his classmate

age = input("What is your age? ")
age_diff = int(age) - 21
if age_diff < 0:
    positive_age = age_diff * -1
    print("Ali's and your age difference is", positive_age)
else:
    print("Ali's and your age difference is", age_diff)
