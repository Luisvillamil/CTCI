# 2-2 Return Kth to last:
# leetcode problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Iterative O(1) space solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node1 = node2 = head
        for _ in range(n):
            node1 = node1.next
        if not node1:
            return head.next
        while node1.next:
            node1 = node1.next
            node2 = node2.next
        node2.next = node2.next.next
        return head
