"""
https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:
"""

def loop_size(node):
    statr_of_loop = find_start(node)
    current_node = statr_of_loop
    count = 1

    while current_node.next != statr_of_loop:
        current_node = current_node.next
        count += 1

    return count

def find_start(node):
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow