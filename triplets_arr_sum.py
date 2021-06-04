output
# [[9, 8, 1], [15, 2, 1], [9, 7, 2], [8, 7, 3],
# [9, 6, 3], [8, 6, 4], [9, 5, 4], [7, 6, 5]]

# Using set 
arr=[1,2,3,4,5,6,7,8,9,15]
target = 18
i=0
res=[]
while i < len(arr):
    new_target = target-arr[i]
    r=[]
    j=i+1
    s1=set()
    for j in range(i+1,len(arr)):
        if new_target - arr[j] in s1:
            r.append(arr[j])
            r.append(new_target - arr[j])
            r.append(arr[i])
            res.append(r)
            r=[]
        else:
            s1.add(arr[j])
        j+=1
    i+=1
print(res)

# Implementing with sorting and two pointer 
# sorting --> NlogN, iteration --> N^2, 
# total --> N^2 + NlogN
# [[9, 8, 1], [15, 2, 1], [9, 7, 2], [8, 7, 3],
# [9, 6, 3], [8, 6, 4], [9, 5, 4], [7, 6, 5]]

arr=[1,8,9,15,2,3,4,5,6,7]
arr.sort()
target = 18
i=0
res=[]
while i < len(arr):
    new_target=target-arr[i]
    # Pair sum problem 
    # apply two pointer approch
    
    r=[]
    left=i+1
    right=len(arr)-1
    while left < right:
        if new_target-arr[left] == arr[right]:
            r.append(arr[i])
            r.append(arr[left])
            r.append(arr[right])
            res.append(r)
            r=[]
            left+=1
            right-=1
        elif new_target-arr[left] > arr[right]:
            left+=1
        elif new_target-arr[left] < arr[right]:
            right-=1
    i+=1
        
            
            
    
