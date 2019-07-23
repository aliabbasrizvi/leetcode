# WIP
class Solution(object):
  def get_combined_sum(self, nums, start, end, current_player):
    if start == end:
      return current_player * nums[start]

    sum_1 = nums[start] * current_player + self.get_combined_sum(nums, start + 1, end, -current_player)
    sum_2 = nums[end] * current_player + self.get_combined_sum(nums, start, end - 1, -current_player)

    return current_player * max(current_player * sum_1, current_player * sum_2)

  def PredictTheWinner(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return self.get_combined_sum(nums, 0, len(nums) - 1, 1) >= 0

if __name__ == '__main__':
  s = Solution()
  nums = [1, 5, 233, 7]
  print s.PredictTheWinner(nums)