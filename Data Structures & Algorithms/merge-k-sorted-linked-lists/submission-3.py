# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        k = len(lists)
        new_lists = []

        def mergeLists(list1, list2):
            dummy = ListNode()
            node = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            
            if list1:
                node.next = list1
            if list2:
                node.next = list2
            
            return dummy.next
        
        i = 1
        new_list = lists[0]
        
        while i < k:
            new_list = mergeLists(new_list, lists[i])
            print(f'{i}: {new_lists}')
            i += 1
        
        return new_list
            
            

        



        

        
        