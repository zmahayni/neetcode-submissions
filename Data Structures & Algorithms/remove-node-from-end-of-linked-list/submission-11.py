# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        i = 1

        remove = prev
        node = ListNode()
        node.next = prev

        while i < n:
            i += 1
            node = node.next
            remove = remove.next

        if i == n:
            node.next = remove.next
        if n == 1:
            prev = node.next
                
        curr = prev
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
            




