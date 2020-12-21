class DoubleLinkedList(object):
  def __init__(self, key, val, prev, nxt):
    self.key = key
    self.val = val
    self.prev = prev
    self.nxt = nxt

class LRUCache(object):
  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.total_count = 0
    self.capacity = capacity
    self.latest = None
    self.earliest = None
    self.value_map = {}

  def remove(self, node):
    if node.prev is not None:
      node.prev.nxt = node.nxt
    else:
      self.latest = node.nxt

    if node.nxt is not None:
      node.nxt.prev = node.prev
    else:
      self.earliest = node.prev

  def add_at_top(self, node):
    node.prev = None
    node.nxt = self.latest
    if self.latest is not None:
      self.prev = node

    self.latest = node
    if self.earliest is None:
      self.earliest = self.latest

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    node = self.value_map.get(key)
    if node is None:
      return -1

    self.remove(node)
    self.add_at_top(node)
    return node.val

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: None
    """
    node = self.value_map.get(key)
    if node is not None:
      node.val = value
      self.remove(node)
      self.add_at_top(node)
      return

    node = DoubleLinkedList(key, value, None, None)
    if self.total_count < self.capacity:
      self.total_count += 1
    else:
      self.add_at_top(node)
      self.remove(self.earliest)
