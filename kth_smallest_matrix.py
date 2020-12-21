class Solution(object):
  def find_kth_small(self, matrix, ranks, k, next_rank):
    if next_rank == k:


  def kthSmallest(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    n = len(matrix)

    total_nums = n * n
    i = 0
    j = 0

    ranks = [[0] * n] * n

    return self.find_kth_small(matrix, ranks, k, 1)








matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8


s = Solution()
print s.kthSmallest(matrix, k)
