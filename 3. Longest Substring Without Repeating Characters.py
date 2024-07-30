class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        cmap= {}
        maxl = 0
        start = 0
        for i in range(len(s)):
            if s[i] in cmap and cmap[s[i]]>= start:
                start = cmap[s[i]] + 1
            cmap[s[i]] = i
            maxl = max(maxl,i-start+1)
        return maxl

