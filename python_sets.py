# . Create a set containing your favorite colors. Assume (yellow - green)

set1={'yellow','green'}
print(set1)

#. Are {'white', 'blue'} part of your favorite colors (answer in two different ways)

set2={'white', 'blue'}

res=set2.issubset(set1)
print(res)

#. Are your favorite colors part of{'white', 'blue', 'brown', 'red', 'yellow', 'green', 'pink'} (answer in two different
#ways)

set2={'white', 'blue', 'brown', 'red', 'yellow', 'green', 'pink'}
res1=set1.issubset(set2)
print(res1)
res2=set1 <= set2
print(res2)

#. Determine how many items in your set

length=len(set1)
print(length)

# Assume you have s1= {10, 23, 65, 78, 90, 54}:
s1= {10, 23, 65, 78, 90, 54}
print(s1)
# Find the minimum number in s1

min_n=min(s1)
print(min_n)
# Find the maximum number in s1

max_n=max(s1)
print(max_n)

#. Find the summation of s1 set numbers

sum=sum(s1)
print(sum)


#. Add 100 to s1

s1.add(100)
print(s1)

#. Find the difference between s1 and s2 where
# s2 = {66, 77, 88, 65, 10} (answer in two different ways)

s2 = {66, 77, 88, 65, 10}

res1=s1.difference(s2)
res2=s1-s2
print(res1)
print(res2)

#. What are the shared numbers between s1, s3 where
#s3= {67, 78, 9, 11, 12} (answer in two different ways)

s3= {67, 78, 9, 11, 12}

res1=s1.intersection(s3)
res2=s1&s3
print(res1)
print(res2)

#g. Find the union of s1, s4 where s4 = {'w', 'p', 'q'}
#(answer in two different ways)

s4 = {'w', 'p', 'q'}

res1=s1.union(s4)
res2=s1 | s4

print(res1)
print(res2)