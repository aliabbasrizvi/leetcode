class Solution(object):
  def get_median(self, numbers):
    if len(numbers) == 0:
      return
    if len(numbers) % 2 == 1:
      return numbers[len(numbers) / 2]
    else:
      return float(numbers[len(numbers) / 2] + numbers[len(numbers) / 2 - 1]) / 2

  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    return self.get_median(nums1)


if __name__ == '__main__':
  s = Solution()
  print s.findMedianSortedArrays([1, 3], [2])
  print s.findMedianSortedArrays([1, 2], [3, 4])
