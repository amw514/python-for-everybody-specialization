# Dictionary

new_dic = {}

new_dic['a'] = 1
new_dic['b'] = 2
new_dic['c'] = 3
new_dic['d'] = 4
new_dic['e'] = 5

print(new_dic)

# Dictionary names count

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)


names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
count = {}
if names in count:
	x = count[names]
else:
	x = 0
    
x = count.get(names,0)
print(count)


# ANother way to count values

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
count = dict()

for name in names:
    count[name] = count.get(name,0) +1
    
print(count)
    

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}

print(list(jjj))


print(jjj.values())


print(jjj.keys())
print(jjj.items())


jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}

for i,j in jjj.items():
    print(i, j)