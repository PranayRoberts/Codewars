""" Example: wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]"""


def wave(people):
    l=len(people)
    a=[]
    for i in range(l):
        s=""
        if people[i]==" ":
           continue
        else:
            s= people[:i] + people[i].upper() + people[i+1:l]
            a.append(s)
        
    return a

#return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
