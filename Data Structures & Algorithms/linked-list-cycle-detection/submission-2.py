# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        faster = head
        while faster and faster.next:
            
            cur = cur.next
            faster = faster.next.next
            if cur == faster:
                return True

        return False
        