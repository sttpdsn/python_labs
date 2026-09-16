s = input()
first, second = 0, 0
for i in range(len(s)):
    if s[i].isupper():
        first = i
        break

for i in range(len(s)):
    if s[i].isdigit():
        second = i+1
        break


dist = second - first

res = ""
for i in range(first, len(s), dist):
    res += s[i]
    if s[i] == ".":
        break
    
print(res)