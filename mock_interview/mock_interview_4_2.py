# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    arr1 = []
    arr2 = []

    while l1 is not None:
      arr1.append(l1.val)
      l1 = l1.next

    while l2 is not None:
      arr2.append(l2.val)
      l2 = l2.next

    idx_arr1 = len(arr1) - 1
    idx_arr2 = len(arr2) - 1

    prev_node = None
    new_node = None
    carry_over = 0
    while idx_arr1 >= 0 or idx_arr2 >= 0:
      if idx_arr2 < 0:
        summed_digit = arr1[idx_arr1] + carry_over
      elif idx_arr1 < 0:
        summed_digit = arr2[idx_arr2] + carry_over
      else:
        summed_digit = arr1[idx_arr1] + arr2[idx_arr2] + carry_over

      carry_over = summed_digit / 10
      summed_digit %= 10
      new_node = ListNode(summed_digit, next=prev_node)
      prev_node = new_node
      idx_arr2 -= 1
      idx_arr1 -= 1

    if carry_over > 0:
      new_node = ListNode(carry_over, prev_node)

    return new_node
