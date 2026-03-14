#### Fimnnd the maximum and minimum of an array 
## Write a function to find the maximum and  minimum elements of an array 
## Iterate through the array , updating the maximum and minimum as you go 

# def find_max_min(arr):
#     maximum = arr[0]
#     minimum = arr[0]

#     for num in arr:
#         if num > maximum:
#             maximum = num
#         if num < minimum:
#             minimum = num

#     return maximum, minimum


# arr = [12, 45, 7, 89, 23, 5]

# maximum, minimum = find_max_min(arr)

# print("Maximum:", maximum)
# print("Minimum:", minimum)


# n = int(input())
# # -------- #
# a = int(input())
# b = int(input())
# # ---------------- #
# a,b = map (int,input().split())
# #--------------------------------#
# a,b,c = map (int,input().split())
# # ---------------------------------#
# arr = list(map(int , input().split()))
# #-------------------------------------#
# arr = eval(input())

### remove duplicates from unsorted array : 

# def remove_duplicate(arr):
#     result = []
#     for num in arr:
#         if num not in result:
#             result.append(num)
#     return result


# if __name__ == '__main__':
#     arr = [3,2,3,1,4]
#     res = remove_duplicate(arr)
#     print(res)


####### Pattern #########
# 1 10
# 2 9
# 4 7
# 5 6

# for i in range(1, 6):
    
#     if i == 3:
#         continue
    
#     print(i, 11 - i)

arr = list(range(1,11))
i = 0
j = len(arr) - 1

while i < j:
    
    if arr[i] == 3:
        i += 1
        j -= 1
        continue
        
    print(arr[i], arr[j])
    
    i += 1
    j -= 1