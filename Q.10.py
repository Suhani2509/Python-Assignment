lst = []
for i in range(1500,2701):
    if(i%5==0 and i%7==0):
        lst.append(i)
print("Number divisible by 7 and 5 are: ",lst)
