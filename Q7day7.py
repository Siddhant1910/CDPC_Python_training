## https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/ ##

# L = int(input().strip())
# N = int(input().strip())

# for i in range(N):
#     w, h = map(int, input().split())
    
#     if w < L or h < L:
#         print("UPLOAD ANOTHER")
#     elif w == h:
#         print("ACCEPTED")
#     else:
#         print("CROP IT")


### https://www.hackerearth.com/problem/algorithm/monk-and-rotation-3-bcf1aefe/ ##

# T = int(input())

# for i in range(T):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
    
#     K = K % N
#     A = A[-K:] + A[:-K]
#     print(*A)

### https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/?utm_source=chatgpt.com ###

# S = input()
# result = ""

# for ch in S:
#     if ch.islower():
#         result += ch.upper()
#     else:
#         result += ch.lower()

# print(result)


## FInd majority element :
## Question: Find the majority element in an array of size n. The majority element is the element that appears more than n/2 times. You may assume that the array is non-empty and the majority element always exists in the array.

n = list(map(int, input().split()))

candidate = None
count = 0

for num in n:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)
