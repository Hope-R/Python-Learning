x = 50

def func(x):
    print(f"x is {x}")

    # Local assignment
    x = 200
    print(f"x is locally assigned to {x}")

func(x)