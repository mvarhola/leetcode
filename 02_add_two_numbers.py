# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        num2 = []
        
        num1.append(l1.val)
        while l1.next is not None:
            l1 = l1.next
            num1.append(l1.val)
        
        num2.append(l2.val)
        while l2.next is not None:
            l2 = l2.next
            num2.append(l2.val)

        fullnum1 = 0
        for i in range(0,len(num1)):
            fullnum1 += num1[i]*(10**i)
        
        fullnum2 = 0
        for i in range(0,len(num2)):
            fullnum2 += num2[i]*(10**i)
            
        fullnum = fullnum1+fullnum2
        
        reverse = 0
        nodelist = []
        while fullnum > 0:
            remainder = fullnum % 10
            nodelist.append(ListNode(remainder))
            reverse = (reverse*10) + remainder
            fullnum = fullnum // 10
            
        for i in range (0, len(nodelist)-1):
            nodelist[i].next = nodelist[i+1]
        
        if len(nodelist) != 0:
            return nodelist[0]
        else:
            return ListNode(0)

