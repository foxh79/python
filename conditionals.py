good_credit = True
has_high_income = True

#logical operator or
if good_credit or has_high_income: 
    print("You get the loan!")
else:
    print("Sorry, you don't qualify for a loan")

#logical operator and
if good_credit and has_high_income:
    print("You get the loan!")
else:
    print("sorry, you dont qualify for a loan")
    
#logical operator not
if not good_credit and not has_high_income:
    print("sorry, you dont qualify for a loan")
else:
    print("You get the loan!")
