
# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the program:


try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("What is your rate? "))
except:
    print("Error, please enter numeric input")
    quit()
if hrs > 40:
    bonus = (hrs - 40) * (1.5 * rate)
    total_rate = (rate * 40) + bonus
    print(total_rate)
else:
    total_rate = (rate * hrs)
    print(total_rate)

