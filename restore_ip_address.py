class Solution(object):
  def findIps(self, s, remaining_literals):
    if len(s) < remaining_literals or len(s) > remaining_literals * 3:
      return []

    if remaining_literals == 1:
      if int(s) <= 255:
        return [str(int(s))]
      else:
        return []

    ip_list = []
    for i in xrange(3):
      ip_literal = str(int(s[:i+1]))
      remaining_ip = s[i+1:]
      sub_ip_list = []
      if int(ip_literal) <= 255:
        sub_ip_list = self.findIps(remaining_ip, remaining_literals - 1)

      for ips in sub_ip_list:
        ip_list.append('.'.join([ip_literal, ips]))

    return set(ip_list)

  def restoreIpAddresses(self, s):
    if len(s) < 4 or len(s) > 12:
      return []

    potential_ips = self.findIps(s, 4)
    all_ips = []
    for ip in potential_ips:
      if len(ip) == 3 + len(s):
        all_ips.append(ip)

    return all_ips

