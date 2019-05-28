def sapxep(lst):
    for j in range(0,len(lst)-2):
        for i in range(0,len(lst)-1-j):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst
