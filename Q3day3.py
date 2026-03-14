

# n = int(input("enter no: "))
# x = int(input("enter no: "))
# sum = 1
# for i in range(1,n):
#     sum = sum +(x**i)/i
# print(sum)

# for i in range(1, 5): # rows
#     for j in range(1, 5):  # cols
#         print(j , end = " ")
#     print() # new line

# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3
# 4 4 4 4    
####### -------outputs---------##########
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4
# 1 2 3 4

# n= 1
# for i in range(1, 5): # rows
#     for j in range(1, 5):  # cols
#         print(n, end = "\t") 
#         n = n + 1
#     print() # new line
# 1       2       3       4
# 5       6       7       8
# 9       10      11      12
# 13      14      15      16


##### ASCII value of character #########
# A = 65 , a= 97 , 0 = 48
# B = 66 , b = 98 , 1 = 49
# C = 67 , c = 99 , 2 = 50
# D = 68 , d = 100 , 3 = 51

# n= 65
# for i in range(1, 5): # rows
#     for j in range(1, 5):  # cols
#         print(chr(n), end = "\t") 
#         n = n + 1
#     print() # new line

# A       B       C       D
# E       F       G       H
# I       J       K       L
# M       N       O       P


######### ----------------------------- #################

# for i in range(1, 5): # rows
#     for j in range(1, i+1):  # cols
#         print(i, end = "\t") 
#     print() # new line

# 1
# 2       2
# 3       3       3
# 4       4       4       4

for i in range(4,0,-1):   # rows
    for j in range(i):    # cols
        print("*", end="\t")
    print()