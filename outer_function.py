

def outer_function (x):

    def inner_function(x):
        
        if x == 0:
            pass
        else:
            num = 1
            while x > 0:
                num *= x
                x -= 1
        return num
    
    return inner_function(x)

print(outer_function(5))


