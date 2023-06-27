
ls = input("enter your nums--->>")

ls = ls.split(',')

def is_sorted (ls):
    num = 1
    for i in range(len(ls)-1):

        if int(ls[i]) <= int(ls[i + 1]):
            num *= 1

        if int(ls[i]) > int(ls[i + 1]):
            num *= 0

    return num
    
print(is_sorted(ls))




















