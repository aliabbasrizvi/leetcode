import sys
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
  def get_slope(self, point1, point2):
    if point1.x == point2.x and point1.y == point2.y:
      return
    if point1.x == point2.x:
      return sys.maxint
    return float(point2.y - point1.y) / (point2.x - point1.x)

  def maxPoints(self, points):
    """
    :type points: List[Point]
    :rtype: int
    """
    max_points = 0
    for point1 in points:
      for point2 in points:
        slope = self.get_slope(point1, point2)


    return max_points