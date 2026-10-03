# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        idx = 1
        curr = prev
        while curr:
            if idx == n-1:
                if curr.next:
                    curr.next = curr.next.next
                    break
                else:
                    curr.next = None
                    break
            elif idx == n:
                if curr.next is None:
                    curr = None
                    return curr
                else:
                    temp = curr.next
                    curr = None
                    prev = temp
                    break
            curr = curr.next
            idx += 1

        head = prev

        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


        
