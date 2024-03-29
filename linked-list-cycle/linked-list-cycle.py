# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return
        
        slow = head
        fast = head.next
        
        
        while fast:
            if not fast or not fast.next:
                return
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False