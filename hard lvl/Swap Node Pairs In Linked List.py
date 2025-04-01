"""
https://www.codewars.com/kata/59c6f43c2963ecf6bf002252/train/python

You are given the head node of a singly-linked list. Write a method that swaps each pair of nodes in the list, then returns the head node of the list. You have to swap the nodes themselves, not their values.

Example:

(A --> B --> C --> D) => (B --> A --> D --> C)

The swapping should be done left to right, so if the list has an odd length, the last node stays in place:

(A --> B --> C) => (B --> A --> C)

The list will be composed of Nodes of the following specification:



recursive method

from preloaded import Node
def swap_pairs(head):
    if head == None or head.next == None:
        return head

    A, B, C = head, head.next, head.next.next

    B.next = A
    A.next = swap_pairs(C)

    return B



"""
from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new_head = head.next
    previous_node = None
    current_node = head

    while current_node and current_node.next is not None:
        first_node = current_node
        second_node = current_node.next

        first_node.next = second_node.next
        second_node.next = first_node

        if previous_node:
            previous_node.next = second_node

        previous_node = first_node
        current_node = first_node.next

    return new_head
