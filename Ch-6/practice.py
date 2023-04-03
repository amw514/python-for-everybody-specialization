# indexing

fruit = "Strawberry"

index = 0

while index < len(fruit):
    print(index,fruit[index])
    index +=1
print()
for index,letter in enumerate(fruit):
    print(index,letter)

print("--------------------------------")
#Slicing strings

s = "Monty Python String"
print(s[4:7])

#Replacing and slicing strings

msg = "From stephen.marquard@uct.ac.za Sat 22/12/2003"
new_msg = msg.replace("@uct.ac.za", "@hellobuddy.com")
print(new_msg)

