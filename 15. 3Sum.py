

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
    

# Two Pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums):
        
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1 , len(nums) -1
            
            while l<r:
                
                t = a + nums[l] + nums[r]
                if t > 0:
                    r -=1
                elif t<0:
                    l +=1   
                else:
                    res.append([a,nums[r],nums[l]])
                    r-=1
                    l+=1  

                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return res
            

