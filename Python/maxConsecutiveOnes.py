#%%
array = [1,1,0,1,1,1]
def findMaxConsecutiveOnes(nums):
    maxCount = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count = 0
    return maxCount

result = findMaxConsecutiveOnes(array)
print(result)
# %%
