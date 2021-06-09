# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 
#  for 101 
#  (2^2 * 1) + (2^1 * 0) + (2^0 * 1) = 5
#  can be rewritten as 
#  2( (2^1 * 1) + (2^0 * 0)) + 1 = 5
#  2( 2 ( (2^0 * 1) + 0 ) ) + 1 = 5

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        while head is not None:
            value = value*2 + head.val
            head = head.next
        return value
        
