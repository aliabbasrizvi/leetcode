class Solution(object):
  def largestValues(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    process_elements = []
    if root:
      process_elements.append(root)

    largest_values = []
    while len(process_elements) != 0:
      largest_values.append(max(node.val for node in process_elements))
      temp_elements = []
      for element in process_elements:
        if element.left:
          temp_elements.append(element.left)
        if element.right:
          temp_elements.append(element.right)
      process_elements = temp_elements

    return largest_values
