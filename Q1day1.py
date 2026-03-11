# ## find last digit number 
# n = int(input("Enter any value : "))
# res = n%10 
# print (res)

## Sum of 2 digit number , n0 = 45 then 4+5 

# n = int(input("Enter any value : "))
# n1 = n%10
# n2 = n//10
# res = n1+n2
# print(res)

## Sum of 3 digit number , 123

# n = int(input("Enter any value : "))
# n1 = n%10  # 3
# n = n//10 #12
# n2 = n%10 #2
# n3 = n//10 #1

# res = n1+n2+n3
# print(res)


## sum of 5 digit number 12345
n = int(input("Enter any value : "))
n1 = n%10  # 5
n = n//10 #1234
n2 = n%10 #4
n = n//10 #123
n3 = n%10 #3
n = n//10 #12
n4 = n %10 #2
n5 = n// 10 #1

res = n1+n2+n3+n4+n5
rev = n1*10000 + n2*1000 + n3*100 + n2*10 + n1
print(res)
print(rev)