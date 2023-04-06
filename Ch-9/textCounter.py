line_text = input("Please enter a line: ")
counts = dict()
split_line = line_text.split()
for word in split_line:
    counts[word] = counts.get(word, 0) + 1
print(counts)

