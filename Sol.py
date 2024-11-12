count=0 
n=len(nums)
for i in range(n):
    suma=0 
    for j in range(i,n):
        suma+=nums[j] 
        if suma==k:
            count+=1 
return count  
