class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        f = head
        s = head
        while (f and f.next):
            s = s.next
            f= f.next.next
        return s