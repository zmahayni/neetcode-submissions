# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        prev = None
        
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp
        
        list2 = prev
        list1 = head
        dummy = node = ListNode()
        count = 1
        while list1 or list2:
            if (count % 2) != 0:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
                
            count += 1
            node = node.next


        

        

        



        



            


        



        
        