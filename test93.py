def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]

for item in filter(check_even,mynums):
    print(item)

a = list(filter(check_even,mynums))
print("\n\nHere you go again: ",a)