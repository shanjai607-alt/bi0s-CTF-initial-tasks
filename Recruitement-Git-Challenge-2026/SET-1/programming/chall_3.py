s = input()
ans = ""

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c in s:
    if c in lower:
        i = lower.index(c)
        ans += lower[(i + 2) % 26]

    elif c in upper:
        i = upper.index(c)
        ans += upper[(i + 2) % 26]

    else:
        ans += c

print(ans)