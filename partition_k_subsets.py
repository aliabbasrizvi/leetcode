class Solution(object):
  def canPartitionKSubsets(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    total_sum = sum(nums)
    is_divisible = total_sum % k == 0

    if not is_divisible:
      return False

    expected_sum = total_sum / k
    sorted_nums = sorted(nums)

    start = 0
    end = len(nums) - 1

    if sorted_nums[end] > expected_sum:
      return False

    while sorted_nums[end] == expected_sum:
      end -= 1

    if end == start:
      return True

    current_sum = 0
    next_num = sorted_nums[start] + sorted_nums[end]
    from_start = None
    while end - start > 1:
      current_sum += next_num

      if current_sum == expected_sum:
        current_sum = 0
        if from_start:
          start += 1
        else:
          end -= 1
        continue

      if current_sum < expected_sum:
        if current_sum + sorted_nums[end - 1] < expected_sum:
          next_num = sorted_nums[end - 1]
          from_start = False
          end -= 1
        else:
          next_num = sorted_nums[start + 1]
          start += 1
          from_start = True

      else:
        return False

    return True
