def greet_user():
    print ("Hello")
    print ("How are you?")


print("Start")
greet_user()
print("Finished function")

#with parameters
def greet_user(username):
    print ("Hello")
    print ("How are you?")
    print(f"Hello, {username}")


greet_user("Foxh")
greet_user("Mwau")

#for numerical values, use keyword arguments
def calc_cost(total=70, shipping=14, discount=0.2):
#use positional arguments first then keyword arguments when mixing them
 print(f"Total: {total}")
 print(f"Shipping: {shipping}")
 print(f"Discount: {discount}")
 print(f"Cost: {total + shipping - (total * discount)}")

def square(number):
    return number * number


print(square(5))