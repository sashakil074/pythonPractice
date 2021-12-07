list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]
list_1.pop(3)
print(list_1)
list_1 = [12, 32, 3, -4, 6, 9, 45, 32, 8]
l=len(list_1)
print(l)
max_n=max(list_1)
print(max_n)
min_n=min(list_1)
print(min_n)
sum=sum(list_1)
print(sum)
list_1.append(9)
print(list_1)
list_2=['a','v','d']
list_1.extend(list_2)
print(list_1)

list_1.remove(-4)
print(list_1)

list_1.insert(1,'r')
print(list_1)

list_1.reverse()
print(list_1)

res=list_1.index(45)
print(res)

c=list_1.count(32)
print(c)

list_1.pop(3)
print(list_1)

list_1.clear()
print(list_1)