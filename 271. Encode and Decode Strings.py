class Solution:

    def encode(self, strs: List[str]) -> str:
        ss = ""
        for s in strs:
            ss += str(len(s)) + "#"+ s
        return ss

    def decode(self, s: str) -> List[str]:
        list = []
        ss= s
        l = 0
        i = 0
        while l<len(ss):
            if ss[i+1]!="#":
                if ss[i+2]!="#":
                    l += int(ss[i:i+3]) + 4
                    list.append(ss[i+4:l])
                    i+=int(ss[i:i+3]) + 4
                else:
                    l += int(ss[i:i+2]) + 3
                    list.append(ss[i+3:l])
                    i+=int(ss[i:i+2]) + 3
            else: 
                l += int(ss[i]) + 2
                list.append(ss[i+2:l])
                i+=int(ss[i]) + 2
        return list
