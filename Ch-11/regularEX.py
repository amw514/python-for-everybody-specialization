# pattern = "world!$” what does it mean by $ in regex?

import re

pattern = "world!$"
string1 = "Hello, world!"
string2 = "Hi there, world!"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)

print(match1)  # Output: <re.Match object; span=(7, 13), match='world!'>
print(match2)  # Output: <re.Match object; span=(10, 16), match='world!'>

# pattern = "^Hello” what does it mean by ^  in regex?

import re

pattern = "^Hello"
string1 = "Hello, world!"
string2 = "Hi there, Hello"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)

print(match1)  # Output: <re.Match object; span=(0, 5), match='Hello'>
print(match2)  # Output: None

#pattern = "(ab)+” what does it mean by () in regex

import re

pattern = "(ab)+"
string = "The string contains abababab and abab."

match = re.search(pattern, string)

print(match.group())  # Output: abababab



#pattern = "cat|dog” what does it mean by | in regex

import re

pattern = "cat|dog"
string1 = "I have a cat and a dog."
string2 = "I have a bird and a fish."

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)

print(match1.group())  # Output: cat
print(match2)  # Output: None

#pattern = "colou?r” what does ? means in regex

import re

pattern = "colou?r"
string1 = "The color of the sky is blue."
string2 = "The colour of the leaves is green."

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)

print(match1.group())  # Output: color
print(match2.group())  # Output: colour

# pattern = r"john\w+@(\w+\.)*com” what does + means here in regex?

import re

string = "aaab"
pattern = "a+b"

matches = re.findall(pattern, string)

print(matches)

# pattern = "a.b”  what does  . means here? in regexx


import re
string = "Hello, World!"
pattern = "H.llo"
matches = re.findall(pattern, string)
print(matches) # ['Hello']

