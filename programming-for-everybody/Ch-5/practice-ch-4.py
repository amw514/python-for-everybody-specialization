# While loop

n = 5
while n  > 0:
    print(n)
    n-=1
print("Blastoff!")


# For Loop 
#Definite Loop

for i in [5,4,3,2,1,0]:
    print(i)
print("Blastoff!")

# Another definite loop

friends = ['Tofeeq',"Hamza","Ali","Ahmad"]

for friend in friends:
    print("Hello dear "+friend)   
    
# Largest number so far 

largest_so_far = -1
numbers_list = [21,3,13,56,7,45,63,23,54,34]
for num in numbers_list:
    if num > largest_so_far:
        largest_so_far = num
    print(f"Largest number is {largest_so_far} and current number is {num}")
print("Largest number", largest_so_far)

# Sum in Loop

zork = 0
print("Before Sum = 0")
for thing in numbers_list:
    zork += thing
    print(f"Sum is {zork} and current number is {thing}")
print("Sum is", zork)

# FInding the average in a loop

count = 0
sum = 0 
print("Before FInding", count, sum)
for thing in numbers_list:
    count += 1
    sum += thing
    print(f"Sum is {sum} and current number is {thing} and count is {count}")
print("Sum is", sum, "Average is", sum/count)

# None value type

smallest = None

for thing in numbers_list:
    if smallest == None:
        smallest = thing
    elif thing < smallest:
        smallest = thing
    print(f"Smallest is {smallest} and current number{thing}")
print("Smallest is", smallest)