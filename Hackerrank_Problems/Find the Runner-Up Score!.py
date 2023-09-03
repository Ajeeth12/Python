
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = map(int, input().split())
arr1 = list(arr)
nos = []
for i in arr1:
    if i < max(arr1):
        nos.append(i)
print(max(nos))
