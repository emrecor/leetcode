

#Bruteforce

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for y in range(i+1,len(nums)):
                for j in range(y+1, len(nums)):
                    if nums[i]+nums[y]+nums[j]==0:
                        dum = [nums[i],nums[y],nums[j]]
                        res.add(tuple(dum))

        return [list(i) for i in res]
    

