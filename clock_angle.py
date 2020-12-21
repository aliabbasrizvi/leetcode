import math

class Solution(object):
  DEGREE_PER_MIN = 6
  DEGREE_PER_HOUR = 30
  def angleClock(self, hour, minutes):
    """
    :type hour: int
    :type minutes: int
    :rtype: float
    """

    minute_angle = minutes * self.DEGREE_PER_MIN
    hour_angle = (hour % 12) * self.DEGREE_PER_HOUR + minutes / 2.0

    difference = math.fabs(minute_angle - hour_angle)
    if difference > 180:
      return 360 - difference

    return difference

