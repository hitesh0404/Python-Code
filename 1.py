import copy
a = [[8, 2, 9, 2], [3, 1, 7, 4], [4, 5, 8, 6], [8, 9, 4, 2]]
b = copy.deepcopy(a)
# b=[]
for i in range(len(a)):
    # b.append(list())
    for j in range(len(a[0])):
        b[i][j]=a[j][len(a)-i-1]
        # b[i].append(a[j][len(a)-i-1])
print(b)
