# List Constants

x = ['a', 'b', 'c', 'd', 'e']
print(x)

for i, n in enumerate(x):
    print(i,n)
    
    
# Average of all numbers

count = 0
sum = 0
while True:
    value = input('Enter the number here: ')
    if value == 'done': break
    value = int(value)
    count += 1
    sum = sum + value
average = sum/count
print(average)


# Average using Data Structures

num = list()
while True:
    value1 = input('Enter the number here: ')
    if value1 == 'done': break
    value1 = int(value1)
    num.append(value1)
average1 = sum(num)/ len(num)
print(average1)


# Using lists to split and take a portion of the text

email_msg = "From stephen.marquard@uct.ac.za Sat Jan"
split_email = email_msg.split()
email = split_email[1]
domain_email = email.split("@")
domain = domain_email[1]
print(domain)
