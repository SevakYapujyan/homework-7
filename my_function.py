

x = 10

def my_function (a):
    
    global x
    print(x)

    x = 20
    print(x)

print(my_function(x))
