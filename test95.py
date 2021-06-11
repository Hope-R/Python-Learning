names = ["Rajeev","Jason","Sinan"]
a = list(map(lambda x: x[0],names))
print(a)

b = list(map(lambda x: x[::-1],names))
print(b)