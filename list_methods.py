numbers = [1, 2, 3, 4, 5, 7, 7]
#add item to the end
numbers.append(6)
print(numbers)

#insert an item at a specific position
numbers.insert(2, 14)
print(numbers)

#remove item
numbers.remove(14)
print(numbers)



#check if an item is in the list
print(70 in numbers)

#remove duplicates
uniques = list(set(numbers))
print(f"List without duplicates: {uniques}")

#sorting lists
numbers.sort()
print(numbers)

#reverse sorting
numbers.reverse()
print(numbers)

#clear list
numbers.clear()
print(numbers)