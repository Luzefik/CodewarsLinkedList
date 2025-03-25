from preloaded import Node
"""
best solution
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_nth(node, index):
  if node and index >= 0: return node if index < 1 else get_nth(node.next, index - 1)
  raise ValueError
"""

def get_nth(node, index):
    if node is None:
        raise ValueError("List is empty")

    probe = node
    length = 0
    while probe:
        length += 1
        probe = probe.next

    if index < 0 or index >= length:
        raise ValueError("Index out of range")

    probe = node
    for _ in range(index):
        probe = probe.next

    return probe
