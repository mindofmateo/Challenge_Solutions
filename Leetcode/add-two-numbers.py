#!/bin/python3

'''--------------------------------------------------------------------------
| Date: 20180523                                                            |
| URL:                                                                      |
| https://leetcode.com/problems/add-two-numbers/description/                |
| Summary:                                                                  |
| Given two linked lists representing two non-negative integers in reversed |
| order, add the two numbers together and return the sum in the form of a   |
| similar reversed-order linked list.                                       |
--------------------------------------------------------------------------'''

# imports:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # This is my solution:
    def addTwoNumbersOriginal(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        m1, m2 = l1, l2
        m3 = ListNode(None)
        returnHead = m3
        while (m1 != None or m2 != None):
            if (m1 != None):
                carry += m1.val
                m1 = m1.next
            if (m2 != None):
                carry += m2.val
                m2 = m2.next
            m3.next = ListNode(carry % 10)
            carry //= 10
            m3 = m3.next
        if (carry == 1):
            m3.next = ListNode(1)
        return returnHead.next
    
    # Another example from the comments section:
    def addTwoNumbersFromCommentSection(self, l1, l2):
        head = ListNode(0)
        current = head
        carry = 0
        
        while l1 != None and l2 != None:
            value = l1.val + l2.val + carry
            if value < 10:
                carry = 0
            else:
                carry = 1
            newNode = ListNode(value%10)
            current.next = newNode
            current = newNode
            l1 = l1.next
            l2 = l2.next
        
        l3 = l1 if l1 else l2
        
        while l3 != None:
            value = l3.val + carry
            if value < 10:
                carry = 0
            else:
                carry = 1
            newNode = ListNode(value%10)
            current.next = newNode
            current = newNode
            l3 = l3.next
        
        if carry == 1:
            newNode = ListNode(1)
            current.next = newNode
            current = newNode
        return head.next

if __name__ == '__main__':
    # I haven't worked out how to pass in test cases yet:
    Solution.addTwoNumbersOriginal(Node1, Node2)

