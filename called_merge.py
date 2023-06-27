

ls_1 = [1,2,3,4,5,6]
ls_2 = [7,8,9]

def megre(ls_1,ls_2):
    i = 0
    j = 0
    ls_merge = []
    while i < len(ls_1) and j < len(ls_2):
        if ls_1[i] <= ls_2[j]:
            ls_merge.append(ls_1[i])
            i += 1
        else:
            ls_merge.append(ls_2[j])
            j += 1

    while i < len(ls_1):
        ls_merge.append(ls_1[i])
        i +=1

    while j < len(ls_2):
        ls_merge.append(ls_2[j])
        j += 1

    return print(ls_merge)

print(megre(ls_1,ls_2))
