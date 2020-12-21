class Solution(object):
  def maxDistToClosest(self, seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    idx = 0
    j = 0
    for idx in range(len(seats)):
      if seats[idx] == 1:
        break

    max_dist = idx
    prev_1 = idx
    for j in range(idx, len(seats)):
      if seats[j] != 1:
        continue

      dist = (j - prev_1) / 2 + (j - prev_1) % 2
      if dist > max_dist:
        max_dist = dist
      prev_1 = j

    dist = j - prev_1
    if dist > max_dist:
      return dist

    return max_dist

s = Solution()
print s.maxDistToClosest([1,0,0,1])
