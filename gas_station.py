# WIP
class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """

    total_gas = sum(gas)
    total_cost = sum(cost)
    total_stations = len(gas)

    if total_cost > total_gas:
      return -1

    for start_station in xrange(total_stations):
      current_gas = 0
      remaining_gas = total_gas
      remaining_cost = total_cost
      for i in xrange(total_stations):
        current_gas += gas[(i + start_station + total_stations) % total_stations]
        remaining_gas -= gas[(i + start_station + total_stations) % total_stations]
        current_gas -= cost[(i + start_station + total_stations) % total_stations]
        remaining_cost -= cost[(i + start_station + total_stations) % total_stations]
        if current_gas < 0:
          break
        if remaining_cost > (current_gas + remaining_gas):
          break

      if current_gas >= 0:
        return start_station

    return -1

s = Solution()
print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print s.canCompleteCircuit([2,3,4], [3,4,3])