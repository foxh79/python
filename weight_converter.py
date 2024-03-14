weight = int(input("Enter your weight: "))
unit = input("L(pounds) or K(Kilograms)? ")

if unit.upper() == "L":
    converted_weight = weight * 0.45
    print(f"You're {converted_weight} kilograms")
else:
    converted_weight = weight / 0.45
    print(f"You're {converted_weight} pounds")
