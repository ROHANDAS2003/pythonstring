lst = [*range(1,20)]
print("\nThe list is: ",lst)

newlst = []
for i in lst[0:5]:
    newlst.append(i)
for i in range(1,6):
    newlst.append(lst[-i])
print("\nNew list is: ",newlst)

sqrlst= []
for i in newlst:
    sqrlst.append(i**2)
print("\nsquares of elements in new lit are: ",sqrlst)

Twoelement = sqrlst[:2]
print("\nSplited squared list having 2 element is: ", Twoelement)
Threeelement = sqrlst[2:5]
print("\nSplited squared list having 3 element is: ", Threeelement)
Fiveelement = sqrlst[5:]
print("\nSplited squared list having 5 element is: ", Fiveelement)