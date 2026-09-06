str = input("Enter string: ")
ans = ""
i = 0

while i < len(str):
    if str[i] == 'x':
        ans = ans + "0"
        i = i + 1

    elif str[i] == 'o':
        if i + 1 < len(str) and str[i + 1] == 'x':
            ans = ans + "1"
            i = i + 2

        elif i + 1 < len(str) and str[i + 1] == 'o':
            ans = ans + "2"
            i = i + 2

print(ans)


