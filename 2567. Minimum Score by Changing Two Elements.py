class Solution:
    def minimizeSum(self, l: List[int]) -> int:
        list = l.copy()
        v= max(list)
        list.sort()
        n = len(list)
        list.pop(n-1)
        list.pop(0)
        v = min(v,(max(list) - min(list)))
        list = l.copy()
        list.sort()
        list.pop(0)
        list.pop(0)
        v = min(v,(max(list) - min(list)))
        list = l.copy()
        list.sort()
        n = len(list)
        list.pop(n-1)
        list.pop(n-2)
        v = min(v,(max(list) - min(list)))
        return v

        
