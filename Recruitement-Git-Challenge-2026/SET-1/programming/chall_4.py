s = input()

count = {}

for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

for c in count:
    print(c + ":", count[c])

print("Reversed string:", s[::-1])