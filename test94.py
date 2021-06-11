mynums = [1,2,3,4,5,6]
a = list(map(lambda num: num ** 2,mynums))
print(a)

b = list(filter(lambda num: num%2 == 0,mynums))
print(b)