l1 = [5, 5, 98, 47, 6, 4, 65, 47, 4, 5]
l2 = []
l3 = []
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
print(l2)
print(l3)

l4 = []
for j in l1:
    if j not in l3:
        l4.append(j)
print(l4)