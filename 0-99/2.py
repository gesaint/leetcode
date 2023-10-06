from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        lr = []
        cur = None
        while l1 or l2 or (carry == 1):
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            listNode = ListNode()
            listNode.val = sum % 10
            listNode.next = None
            carry = sum // 10


            if cur is None:
                cur = listNode
                lr = listNode
            else:
                cur.next = listNode
                cur = listNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return lr