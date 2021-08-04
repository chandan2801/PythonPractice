# cook your dish here
def mainprogram(iterable,x):
    sample=tuple(iterable)
    print(sample)
    n=len(sample)
    print("n",n)
    print("n and x", n and x)
    if not n and x:
        return
    indices=[1]*x
    print(indices)
    yield tuple(sample[i] for i in indices)
    while True:
        print("Hey")
        for i in reversed(range(x)):
            print(i)
            if(indices[i]!=n-1):
                break
            else:
                return
        print("old",i)
        print("old",indices[i:])
        print("old",[indices[i]+1]*(x-i))
        indices[i:]=[indices[i]+1]*(x-i)
        print(indices[i:])
        print("new indices",indices)
        yield tuple(sample[i] for i in indices)

a=mainprogram('PYTHON',3)

print(next(a))
print(next(a))    