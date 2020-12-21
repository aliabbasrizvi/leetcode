class Solution(object):
  def __init__(self):
    self.min_costs = {}

  def get_cost(self, cost, current_idx):
    if current_idx >= len(cost):
      return 0

    remaining_cost = self.min_costs.get(current_idx)
    if remaining_cost:
      total_cost = remaining_cost
    else:
      total_cost = cost[current_idx] + min(self.get_cost(cost, current_idx + 1), self.get_cost(cost, current_idx + 2))
      self.min_costs[current_idx] = total_cost

    return total_cost

  def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    if len(cost) == 0:
      return 0

    if len(cost) == 1:
      return cost[0]

    return min(self.get_cost(cost, 0), self.get_cost(cost, 1))
