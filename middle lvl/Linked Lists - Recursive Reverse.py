"""

https://www.codewars.com/kata/55e725b930957a038a000042/train/python


var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
reverse(list) === 5 -> 6 -> 3 -> 1 -> 2 -> null


Best Practice
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(head, tail=None):
    return reverse(head.next, Node(head.data, tail)) if head else tail
"""

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head

    tail = reverse(head.next)
    last_node = tail


    while last_node.next is not None:
        last_node = last_node.next

    last_node.next = head
    head.next = None

    return tail