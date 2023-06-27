num = (input("writh your num--->>>"))
num1 = list(num)
a = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
b = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
c = [
       "" "one hundred","two hundred ", "three hundred","four hundred","five hundred","six hundred","seven hundred",
       "eight hundred","nine hundred"
]

d = ["thousand"]
ls = []

for i in num1:
    ls.append(int(i))
ll = []
grups_num = []

if int(num) > int(1015):
    print("error")

def inta_str (ls):
    if len(ls) == 4:
        ll.append(d[0])
        ll.append(c[ls[1]])
        if ls[2] > 1:
            ll.append(b[ls[2]])
            ll.append(a[ls[3]])
        elif ls[2] == 1:
            ll.append(a[ls[2]])              #
        else:
            ll.append(a[ls[3]])

    if len(ls) == 3:
        ll.append(c[ls[0]-1])
        if ls[1] > 1:
            ll.append(b[ls[1]])
            ll.append(a[ls[2]])
        if ls[1] == 1:
            ll.append(a[ls[1]])
        if ls[1] == 0:
            if ls[2] != 0:
                ll.append(a[ls[2]])
        
    if len(ls) == 2:
        if ls[0] > 1:
            ll.append(b[ls[0]])
            ll.append(a[ls[1]])
        else:
            ll.append(a[ls[0]+9+ls[1]])
    if len(ls) == 1:
        ll.append(a[ls[0]])

    return ll


inta_str(ls)
print(ll)
 








