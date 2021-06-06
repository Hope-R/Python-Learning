fruits = ["apple", "banana", "cherry", "kiwi", "orange"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)