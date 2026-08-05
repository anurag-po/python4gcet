a = input("Input C or F (c/f) : ").lower()
print("Invalid input" if a not in 'cf')
val = int(input(f"{a.upper()} value : "))
print("Converted Value: ", val * 1.8 + 32 if a == 'c' else (val - 32) / 1.8)
