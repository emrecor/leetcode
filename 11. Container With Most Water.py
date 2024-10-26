

#sacma brute force denemesi calismiyor


nums = [2,2,2]



m = max(nums)

idx = nums.index(m)
nums.remove(m)
maks = 0
a=1
for i in range(idx,len(nums)):
    m1 = max(nums)
    idx1 = nums.index(m1)+a
    
    maks = max(((idx1-idx) * m1),maks)
    nums.remove(m1)
    a+=1