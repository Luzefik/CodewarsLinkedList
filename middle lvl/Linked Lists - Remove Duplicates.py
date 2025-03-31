"""
https://www.codewars.com/kata/55d9f257d60c5fd98d00001b/train/python

Linked Lists - Remove Duplicates

Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes from the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null

If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

The push() and buildOneTwoThree() functions need not be redefined.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head == None:
        return head
    current = head
    next = current.next
    while next:
        if current.data == next.data:
            current.next = current.next.next
            next = current.next
        else:
            current = next
            next = current.next
    return head
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    set_of_dup = set()

    if head is None:
        return None
    if head.next is None:
        return head
    current_node = head
    set_of_dup.add(current_node.data)
    while current_node.next is not None:
        if current_node.next.data in set_of_dup:
            set_of_dup.add(current_node.data)
            current_node.next = current_node.next.next
        else:
            set_of_dup.add(current_node.next.data)
            current_node = current_node.next
    return head

