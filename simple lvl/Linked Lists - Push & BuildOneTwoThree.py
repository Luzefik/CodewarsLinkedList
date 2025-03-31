'''
https://www.codewars.com/kata/55be95786abade3c71000079/solutions/python


Best solution
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    return Node(data, head)

def build_one_two_three():
    return Node(1, Node(2, Node(3)))
'''

def push(head, data):
    if head is None:
        return Node(data)
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
