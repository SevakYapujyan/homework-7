
ls = input("enter your nums--->>")

ls = ls.split(',')

def is_sorted (ls):
    num = 1
    ll = []
    for i in ls:
        ll.append(int(i))
    for i in range(len(ll)-1):

        if int(ll[i]) <= int(ll[i + 1]):
            num *= 1

        if int(ll[i]) > int(ll[i + 1]):
            num *= 0

    return True if num == 1 else False
    
print(is_sorted(ls))




















