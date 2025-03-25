"""
https://www.codewars.com/kata/582c5382f000e535100001a7/train/python

best solution

def linked_list_from_string(s):
    head = None
    for i in s.split('->')[-2::-1]:
        head = Node(int(i),head)
    return head
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    list_of_el = s.split(" -> ")
    list_of_el.pop() 

    head = None
    for i in range(len(list_of_el) - 1, -1, -1):
        try:
            node_value = int(list_of_el[i])
        except ValueError:
            return None
        new_node = Node(node_value, head)
        head = new_node
    return head
