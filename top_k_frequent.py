# WIP
class NumFreq(object):
  def __init__(self, val, count):
    self.val = val
    self.count = count

class Solution(object):
  def insert_into_heap(self, current_heap, num):
    cur_index = len(current_heap) - 1
    if current_heap[cur_index].count > num.count:
      return

    current_heap[cur_index] = num
    next_index = (cur_index - 1) / 2
    while next_index >= 0 and current_heap[next_index].count < current_heap[cur_index].count:
      temp = current_heap[cur_index]
      current_heap[cur_index] = current_heap[next_index]
      current_heap[next_index] = temp
      next_index = (cur_index - 1) / 2

  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    top_nums = [NumFreq(0, 0)] * k
    num_to_count = {}
    for num in nums:
      num_to_count[num] = num_to_count.get(num, 0) + 1

    print num_to_count
    for val, count in num_to_count.iteritems():
      num = NumFreq(val, count)
      self.insert_into_heap(top_nums, num)

    return [num.val for num in top_nums]

s = Solution()
s.topKFrequent([1,1,1,3,3,3,3,2,2,2,2,2,2,3], 3)