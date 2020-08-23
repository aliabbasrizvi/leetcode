# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def build_tree(self, tree_elements):
    tree_nodes = []
    for element in tree_elements:
      if element is not None:
        tree_nodes.append(TreeNode(element))
      else:
        tree_nodes.append(None)

    for idx in xrange(len(tree_nodes) / 2):
      if tree_nodes[idx] is None:
        continue
      tree_nodes[idx].left = tree_nodes[idx * 2 + 1]
      tree_nodes[idx].right = tree_nodes[idx * 2 + 2]

    return tree_nodes

  def get_preorder_traversal_until_val(self, tree_node, val, traversal):
    if tree_node is None:
      return

    traversal.append(tree_node)
    if tree_node == val:
      return
    self.get_preorder_traversal_until_val(tree_node.left, val, traversal)
    self.get_preorder_traversal_until_val(tree_node.right, val, traversal)

  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    traversal1 = []
    traversal2 = []
    self.get_preorder_traversal_until_val(root, p, traversal1)
    self.get_preorder_traversal_until_val(root, q, traversal2)

    print(traversal1)
    print(traversal2)


s = Solution()
tree_nodes = s.build_tree([3,5,1,6,2,0,8,None,None,7,4])
root = tree_nodes[0]
p = tree_nodes[1]
q = tree_nodes[2]
s.lowestCommonAncestor(root, p, q)