class Solution(object):
  def frequencySort(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    num_to_freq = {}
    for num in nums:
      num_to_freq[num] = num_to_freq.get(num, 0) + 1

    freq_to_num = {}
    for num, freq in num_to_freq.iteritems():
      freq_to_num[freq] = freq_to_num.get(freq, [])
      freq_to_num[freq].append(num)

    for freq, num in freq_to_num.iteritems():
      freq_to_num[freq].sort(reverse=True)

    sorted_freq = freq_to_num.keys()
    sorted_freq.sort()

    res = []
    for freq in sorted_freq:
      for num in freq_to_num.get(freq):
        res += [num] * freq

    return res
