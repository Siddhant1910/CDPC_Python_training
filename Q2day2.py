## A number is said to be Peterson if the sum of factorial of each digit is equal to the sum of the number itself 
# ex :- 145 
# 145 = !1 = !4 + !5 = 1+4*3*2*1+5*3*2*1*4
# = 1 +24+120 = 145 
import math 

# n = int(input("Enter any number: "))
# x = n
# res = 0
# sum = 0
# rev =0 
# count = 0


# n = int(input("Enter any 3 digit  value : "))
# x =n 
# n1 = n%10  # 3
# n = n//10 #12
# n2 = n%10 #2
# n3 = n//10 #1

# r1 = math.factorial(n1)
# r2 = math.factorial(n2)
# r3 = math.factorial(n3)

# res = r1 +r2 +r3

# if x == res:
#     print("n is peterson number ")

### Peterson using loop 


# while n>0:
#     digit = n%10 
#     res = res + math.factorial(digit)
#     n = n//10

# if x == res:
#     print("It is a Peterson number")
# else:
#     print("It is not a Peterson number")


########### Count and sum  of digits #######################

# while n>0 :
#     rem = n%10 
#     n = n //10
#     sum = sum + rem
#     res = res +1


# print("The count of digit is : ", res )
# print("The sum of number is : ", sum )


########### Check number is Palindrome or not #############################

# while n>0:
#     rem = n%10
#     rev = rev *10 + rem 
#     n = n//10

# if rev == x:
#     print("number is palindrome")
# else :
#     print("number is not palindrome")

#################### Armstrong number ######################################
# ex :- 153 = 1^3 + 5^3 +3^3

# while n>0:
#     n = n//10
#     count = count + 1 

# n = x 

# while n> 0:
#      rem = n%10
#      sum = sum + rem**count
#      n = n//10

# if x == sum:
#      print("number is armstrong")
# else :
#      print("not armstrong")

    
################ Print Armstrong 1 to 1000 ####################
for i in range(1, 10001):

    n = i
    count = 0
    total = 0

    while n > 0:
        n = n // 10
        count = count + 1

    n = i

    while n > 0:
        rem = n % 10
        total = total + rem ** count
        n = n // 10

    if i == total:
        print(i)

