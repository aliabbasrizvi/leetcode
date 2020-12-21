# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    slow_head = head
    fast_head = head

    cycle_found = False
    while slow_head is not None and fast_head is not None:
      slow_head = slow_head.next
      fast_head = fast_head.next
      if fast_head:
        fast_head = fast_head.next

      if slow_head == fast_head and slow_head is not None:
        cycle_found = True
        break

    return cycle_found