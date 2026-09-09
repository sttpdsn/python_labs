n = int(input())
ochno, zaochno = 0, 0
for _ in range(n):
    surname, name, age, presence = input().split()
    if presence == "True":
        ochno += 1
    else:
        zaochno += 1
print(ochno, zaochno)