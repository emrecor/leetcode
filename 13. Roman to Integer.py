class Solution:
    def romanToInt(self, s: str) -> int:
        t = 0
        i = 0
        if s[i] == "M":
                t+=1000
                i+=1
        elif s[i] == "D":
                t += 500
                i += 1

        if s[i] == "C":
            if s[i + 1] == "M":
                t += 900
                i+=2
            elif s[i + 1] == "D":
                t += 400
                i += 2
            else:
                t += 100
                i += 1

        if s[i] == "L":
                t += 50
                i += 1
        if s[i] == "X":
            if s[i + 1] == "L":
                t += 40
                i += 2
            elif s[i + 1] == "C":
                t += 90
                i += 2
            else:
                t += 10
                i += 1

        if s[i] == "V":
                t += 5
                i += 1

        if s[i] == "I":
            if s[i+1] == "I":

                if s[i+2] == "I":
                    t+=3
                else:
                    t+=2
                
            elif s[i + 1] == "X":
                    t += 9
                    i += 2
            elif s[i + 1] == "V":
                    t += 4
                    i += 2
            else:
                    t += 1
        return t
