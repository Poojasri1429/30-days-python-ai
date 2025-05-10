try:
    num = int(input("Enter a number: "))
    print("Result is", 10 / num)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print("No errors!")
finally:
    print("This will run no matter what.")

