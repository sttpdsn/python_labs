a, b = float(input("a: ").replace(",", ".")), float(input("b: ").replace(",", "."))
sum = a + b
avg = sum / 2
print(f"{sum=:.2f}; {avg=:.2f}")