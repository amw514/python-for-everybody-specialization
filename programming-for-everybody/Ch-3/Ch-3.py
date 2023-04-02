# Chapter 3 Conditional with loops example

for i in range(1,10+1):
    print(i)
    if  i<2:
        print("less than 2")
    print("Done with index",i)
# if-else condition

y = 10

if y < 15:
    print("Less than 15")
else:
    print("Less than 15")
    
    
# Multi way Conditional / if-elif-else
z = 15
if z < 2 :
    print('Small')
elif z < 10 :
    print('Medium')
elif z < 20 :
    print('Big')
elif z < 40 :
    print('Large')
elif z < 100:
    print('Huge')
else :
    print('Ginormous')