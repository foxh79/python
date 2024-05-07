try:
    age = int(input("Enter age:"))
    income = 70000
    risk = income/age

except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("Invalid value")