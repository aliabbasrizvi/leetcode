class Solution(object):
  def get_min_time(self, point1, point2):
    diff_x = point2[0] - point1[0]
    diff_y = point2[1] - point1[1]

    if diff_x == diff_y:
      return abs(diff_x)

    if abs(diff_x) < abs(diff_y):
      return abs(diff_x) + abs(point2[1] - (point1[1] + diff_x))
    else:
      return abs(diff_y) + abs(point2[0] - (point1[0] + diff_y))


  def minTimeToVisitAllPoints(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    total_time = 0
    total_points = len(points)

    if total_points == 0 or total_points == 1:
      return 0

    for idx in range(1, total_points):
      total_time += self.get_min_time(points[idx - 1], points[idx])

    return total_time
