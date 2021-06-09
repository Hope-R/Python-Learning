def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs["food"]))

myfunc(12,22,33,44,fruit="orange",food="banana",animal="dog")