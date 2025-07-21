#%%
from functools import reduce
def findNumsWithEvenNumberofDigits(nums):
    return reduce(lambda count, num: count + (1 if len(str(num)) % 2 == 0 else 0), nums, 0)
findNumsWithEvenNumberofDigits([12, 345, 2, 6, 7896])
# %%