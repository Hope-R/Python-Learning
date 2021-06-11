def splicer(mystring):
    if len(mystring)%2 == 0:
        return "Even"
    else:
        return mystring[0]

names = ["Rajeev","Jason","Sinan"]

#a = splicer(names)
a = list(map(splicer,names))
print(a)