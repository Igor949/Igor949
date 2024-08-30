def print_params(a = 1, b = 'forvard', c = True):
    print(a,b,c)
    print(a,c,b)
c=[1,2,3]

values_list = [1,"tor",False]
values_dict = {'a':3,'b':"rol",'c':True}

values_list_2 = (2,[1,2,3])

print_params() #1 forvard,True
print_params(7,2,1) #7 2 1
print_params("good",1,4) # good,1 4
print_params("step",b=25,c=[1,2,3])
print_params(*c)


print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 42)
