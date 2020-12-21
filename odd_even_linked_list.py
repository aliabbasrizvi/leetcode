# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    if head is None:
      return head

    odd_head = head
    even_head = head.next

    current_odd = head
    current_even = even_head
    switch_even = False
    while current_odd is not None and current_even is not None:
      if not switch_even:
        current_odd.next = current_even.next
        current_odd = current_odd.next
        switch_even = True
      else:
        current_even.next = current_odd.next
        current_even = current_even.next
        switch_even = False

    temp = odd_head
    while temp.next is not None:
      temp = temp.next

    temp.next = even_head
    return odd_head
