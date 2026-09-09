try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result obtained is : ", result)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program finished.")
