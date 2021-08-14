def RandomProgram(f):
    m={}
    print("Comes here first")
    def innerProgram(num):
        print("Comes here second",num)
        if num not in m:
            m[num]=f(num)  #Calls Cal(3)
        print(m)
        print("m[",num,"]",m[num])
        return m[num]
    return innerProgram
@RandomProgram
def Cal(num):
    print("Comes here third and does recursion")
    if num==0:
        return 1
    else:
        return num**2*Cal(num-1) #x**y = pow(x,y) #recursions - 3**2*Cal(2) op - 9*4=36, 2**2*Cal(1) op - 4, 1**2*Cal(0) op - 1, 1

print(Cal(3))

#RandomProgram function is called first and it calls the innerProgram. innerProgram calls Cal function
