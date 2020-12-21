class Solution(object):
  def letterCasePermutation(self, S):
    """
    :type S: str
    :rtype: List[str]
    """
    if len(S) == 0:
      return []

    if len(S) == 1:
      if S[0] >= 'a' and S[0] <= 'z':
        return [S[0], chr(ord(S[0]) - 32)]
      if S[0] >= 'A' and S[0] <= 'Z':
        return [S[0], chr(ord(S[0]) + 32)]
      else:
        return [S[0]]

    received_perms = self.letterCasePermutation(S[1:])
    perms1 = []
    if S[0] >= 'a' and S[0] <= 'z':
      perms1 = [chr(ord(S[0]) - 32) + perm for perm in received_perms]
    if S[0] >= 'A' and S[0] <= 'Z':
      perms1 = [chr(ord(S[0]) + 32) + perm for perm in received_perms]

    perms2 = [S[0] + perm for perm in received_perms]
    return perms1 + perms2
