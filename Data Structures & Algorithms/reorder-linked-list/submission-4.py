# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_list = slow.next
        slow.next = None

        curr = second_list
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        i = 1

        while head and prev:
            if i == 1:
                temp = head.next
                head.next = prev
                head = temp
                i = 0
            elif i == 0:
                temp = prev.next
                prev.next = head
                prev = temp
                i = 1
        

        # dummy = node = ListNode()
        # node.next = head

        # list1 = head
        # list2 = prev
        
        # i = 1
        # while list1 and list2:
        #     if i % 2 != 0:
        #         node.next = list2
        #         list2 = list2.next
        #     else:
        #         node.next = list1
        #         list1 = list1.next
        #     i += 1
        #     node = node.next
        
        # if not list1:
        #     node.next = list2
        # if not list2:
        #     node.next = list1
        
        
            
        


        
        
        