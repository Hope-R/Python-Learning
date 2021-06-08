def check_even_list(num_list):

    # placeholder for variables
    even_numbers = []

    for x in num_list:
        if x % 2 == 0:
            even_numbers.append(x)
        else:
            pass
    return even_numbers
    # print("Hi") 
a = check_even_list([1,3,5])
print(a)

    