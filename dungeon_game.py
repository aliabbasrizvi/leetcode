# WIP
class Solution(object):
  def get_min_health(self, dungeon, health, x, y):
    current_health = dungeon[x][y]

    if x == len(dungeon) - 1 and y == len(dungeon[0]) - 1:
      health[x][y] = 1 if current_health > 0 else 1 - current_health
      return

    # Move down (x + 1) and right (y + 1)
    if x < len(dungeon) - 1 and y < len(dungeon[0]) - 1:
      self.get_min_health(dungeon, health, x + 1, y)
      self.get_min_health(dungeon, health, x, y + 1)
      health[x][y] = max([min([health[x + 1][y], health[x][y + 1]]) - current_health, 1])
    elif x < len(dungeon) - 1:
      self.get_min_health(dungeon, health, x + 1, y)
      health[x][y] = max([health[x + 1][y] - current_health, 1])
    elif y < len(dungeon[0]) - 1:
      self.get_min_health(dungeon, health, x, y + 1)
      health[x][y] = max([health[x][y + 1] - current_health, 1])

    return

  def calculateMinimumHP(self, dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """
    rows = len(dungeon)
    columns = len(dungeon[0])
    each_row = [0] * columns
    health = [each_row] * rows
    self.get_min_health(dungeon, health, 0, 0)
    return health[0][0]
