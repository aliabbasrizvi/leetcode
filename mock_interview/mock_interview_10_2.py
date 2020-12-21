class Solution(object):
  def findReplaceString(self, S, indexes, sources, targets):
    """
    :type S: str
    :type indexes: List[int]
    :type sources: List[str]
    :type targets: List[str]
    :rtype: str
    """
    lookup = []
    replaced_string = ''
    for i, idx in enumerate(indexes):
      len_source = len(sources[i])
      actual_string = S[idx:idx + len_source]
      if actual_string == sources[i]:
        lookup.append((idx, sources[i], targets[i]))

    if len(lookup) == 0:
      return S

    lookup = sorted(lookup, key=lambda x: x[0])
    idx = 0
    current_item = 0
    while idx < len(S):
      if current_item < len(lookup) and S[idx:idx + len(lookup[current_item][1])] == lookup[current_item][1]:
        replaced_string += lookup[current_item][2]
        idx += len(lookup[current_item][1])
        current_item += 1
      else:
        replaced_string += S[idx]
        idx += 1

    return replaced_string
