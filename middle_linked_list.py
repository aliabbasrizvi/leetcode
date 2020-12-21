# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    temp = head
    double_temp = head

    while double_temp and double_temp.next:
      temp = temp.next
      double_temp = double_temp.next
      if double_temp:
        double_temp = double_temp.next

    return temp
