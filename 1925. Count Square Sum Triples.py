class Solution:
    def countTriples(self, n: int) -> int: 
        i = n
        l = []
        while i>0:         
            c = i*i
            for y in range(1,i):
                a = y*y
                b = math.sqrt(c-a)
                x = b - int(b)
                if b>0 and x == 0:
                    l.append((y,b,i))
            i -=1
        return len(l)