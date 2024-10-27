class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        mx = 0
        while l<r:
            mx = max(mx,((r-l)*min(height[l],height[r])))
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                l+=1
        return mx