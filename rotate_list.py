# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    list_count = 0
    temp = head

    while temp is not None:
      list_count += 1
      temp = temp.next

    if list_count == 0:
      return head

    k = k % list_count
    node_end = list_count - k

    if node_end == 0 or k == 0:
      return head

    count = 0
    prev_temp = None
    temp = head
    while count < node_end:
      count += 1
      prev_temp = temp
      temp = temp.next

    new_beg = temp

    while temp.next is not None:
      temp = temp.next

    temp.next = head
    prev_temp.next = None

    return new_beg
