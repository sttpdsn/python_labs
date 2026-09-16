m = int(input("Минуты: "))
hrs, mins = m // 60, m % 60
print(f"{hrs}:{mins:02d}")