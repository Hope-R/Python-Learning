x = 50

def func(x):
    print(f"x is {x}")
    # Local assignment on a global variable
    x = "New value"
    print(f"\nx is now - {x}")
    return x

print(x)

x = func(x)

print(x)

