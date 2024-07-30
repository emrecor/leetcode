


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dummy = {}
        for i in range(len(strs)):
            v = strs[i]
            v = ''.join(sorted(v))
            if dummy.get(v) != None:
                dummy[v].append(strs[i])
            else:
                dummy[v] = [strs[i]]
        return list(dummy.values())

sol = Solution()
print(sol.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))