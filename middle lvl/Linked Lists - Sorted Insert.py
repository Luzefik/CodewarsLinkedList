"""
https://www.codewars.com/kata/55cc33e97259667a08000044//train/python
clever:
class Node(object):
    def __init__(self, data, nxt = None):
        self.data = data
        self.next = nxt

    def sorted_insert(head, data):
        if not head or data < head.data: return Node(data, head)
        else:
        head.next = sorted_insert(head.next, data)
        return head
"""

def sorted_insert(head, data):
    probe = Node(data)

    if head is None or head.data >= data:
        probe.next = head
        return probe
    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    probe.next = current.next
    current.next = probe

    return head