# 1 :
# x=5
# while x>0:
#     print(x,end=" ")
#     x -=2
# output :- 5  3  1

# 2 :How manu times loop will execute
# count = 0
# for i in range(2,10,3):
#     count +=1
# print (count)
# # output :- 3

# 3 : 
# for i in range(4):
#     if i==2:
#         break
#     print(i)
# output :- 0 1

# 4 :       
# x = 10
# while x>0:
#     if x==5:
#         break
#     print(x,end=" ")
#     x-=2
# output :- 10 8 6 4 2

# 5 : 
# for i in range(5,0,-1):
#     print (i)
# output :- 5 4 3 2 1

# 6 :
# while True:
#     print("Hello")
# output :- Infinite loop

#  7 : calculate sum of all even numbers
# sum = 0;
# for i in range(1,21):
#     sum = sum+i
# print("Sum = ",sum)

# 8 : multiplication table of given Number
# num = int(input("Enter your Number : "))
# for i in range(1,11):
#     product = num*i
#     print(f"{num}*{i}=",product)

# 9 : total number of digits in a number
# digit = int(input("Enter your digit : "))
# count = 0
# while(digit>0):
#        remainder = digit%10
#        count=count+1
#        digit=digit//10
# print("Total digits are : ",count)

# 10 : 
num = int(input("Enter your number : "))
if(num<=55):
    print("Number is less or equal to 55")
    if(num>45):
       print("Number is above 45")
elif(num>55):
    print("Number is greater than 55")
else:
    print("Invalid!!")
