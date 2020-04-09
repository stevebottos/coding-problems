# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        add_one = 0        
        newList = True
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total + add_one
            if newList == False: 
                if num < 10:
                    new = ListNode(num)
                    ptr.next = new
                    ptr = new
                    add_one = 0
                elif num > 10:
                    new = ListNode(num%10)
                    ptr.next = new
                    ptr = new
                    add_one = 1
                else:
                    new = ListNode(0)
                    ptr.next = new
                    ptr = new
                    add_one = 1
                
            else: 
                if num < 10:
                    head = ListNode(num)
                    ptr = head
                    add_one = 0
                elif num > 10:
                    head = ListNode(num%10)
                    ptr = head
                    add_one = 1
                else:
                    head = ListNode(0)
                    ptr = head
                    add_one = 1
                newList = False
                    
        # If there's still a value we'll add it in a node
        if add_one == 1:
            new = ListNode(1)
            ptr.next = new
            ptr = new
            
        return head