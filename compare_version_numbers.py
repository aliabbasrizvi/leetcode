class Solution(object):
  def get_array_representation(self, version1, version2):
    ver_1_array_string = version1.split('.')
    ver_2_array_string = version2.split('.')

    ver_1_array = [int(x) for x in ver_1_array_string]
    ver_2_array = [int(x) for x in ver_2_array_string]

    if len(ver_2_array) > len(ver_1_array):
      ver_1_array = ver_1_array + [0] * (len(ver_2_array) - len(ver_1_array))
    else:
      ver_2_array = ver_2_array + [0] * (len(ver_1_array) - len(ver_2_array))

    return ver_1_array, ver_2_array

  def compareVersion(self, version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    ver_1, ver_2 = self.get_array_representation(version1, version2)
    version_num_count = len(ver_1)

    for idx in xrange(version_num_count):
      if ver_1 > ver_2:
        return 1
      if ver_2 > ver_1:
        return -1

    return 0
