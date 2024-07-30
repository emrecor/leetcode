class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict= {}
        for i,num in enumerate(nums):
            y = target - num
            if y in dict:
                return [i,dict[y]]
            dict[num] = i


            

        