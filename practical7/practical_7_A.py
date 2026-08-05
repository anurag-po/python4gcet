a, b = int(input("a:")), int(input("b:"))

try:
  print(a/b)
except ZeroDivisionError:
  print("Cannot divide by Zero")
