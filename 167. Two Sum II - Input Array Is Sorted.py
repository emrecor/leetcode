class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l,r = 0,len(n)-1
        while l<r:
            c = n[l] + n[r]
            if c>t:
                r-=1
            elif c<t:
                l+=1        
            else:
                return [l+1,r+1]