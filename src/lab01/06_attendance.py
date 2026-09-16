n = int(input("in_1: "))
ochno, zaochno = 0, 0
for i in range(n):
    surname, name, age, presence = input(f"in_{i+2}: ").split()
    if presence == "True":
        ochno += 1
    else:
        zaochno += 1
print("out:", ochno, zaochno)