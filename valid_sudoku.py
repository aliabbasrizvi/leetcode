class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    column_marker = {}
    row_marker = {}
    box_marker = {}

    for i, row in enumerate(board):
      for j, literal in enumerate(row):
        if literal >= '1' and literal <= '9':
          if i in row_marker:
            if literal in row_marker[i]:
              return False
            row_marker[i][literal] = True
          else:
            row_marker[i] = {
              literal: True
            }

          if j in column_marker:
            if literal in column_marker[j]:
              return False
            column_marker[j][literal] = True
          else:
            column_marker[j] = {
              literal: True
            }

          box =


    return True




s = Solution()
print s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print s.isValidSudoku([["8  ","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])