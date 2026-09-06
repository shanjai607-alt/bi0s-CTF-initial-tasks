numbers = [7, 8, 9, 1, 7, 8, 3]
target = 3

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)


if target in numbers:
    print(True)
else:
    print(False)