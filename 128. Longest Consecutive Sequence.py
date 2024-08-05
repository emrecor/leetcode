class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 0
        for n in nums:
            if n-1 not in nums:
                c = 1
                while (n+c) in nums:
                    c +=1
                m = max(c,m)
        return m
