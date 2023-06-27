

n = int(input("write your num -->> "))

m = int(input("write a power of a given number-->> "))

def power(n):

    def power_of(m,n):
        n = n ** m 
        return n
    global m
    return(power_of(m,n))

   
print(power(n))



