# 1 :
lst = [1,2,3,4,5]
print(lst[::-1])
# output :- [5,4,3,2,1]

# 2 :
lst = [10,20,30]
lst.append([40,50])
print(len(lst))
# output :- 4

# 3 : 
lst = [1,2,3]
lst.extend([4,5])
lst.insert(2,10)
print(lst)
# output :- [1,2,10,3,4,5]

# 4 : 
tup = (1,2,3,4)
tup[2] = 10
print(tup)
# Error : Tuples are immutable

# 5 : 
tup = (10,20,30,40,50)
print(tup[-3])
# output :- 30

# 6 : 
set1 = {1,2,3}
set2 = {2,3,4}
print(set1 & set2)
# output :- {2,3}

# 7 :
set1 = {10,20,30,40}
set2 = {30,40,50,60}
diff = set1-set2
print(diff) 
#  Missing method :- diff=set1-set2

# 8 : 
d = {'x':10,'y':20}
d['z']=30
print(d)
# output :- {'x':10,'y':20,'z':30}

# 9 :
d = {'a':10,'b':2,'c':3}
d.pop('b')
print(d)
# output :- {'a':1,'c':3}





