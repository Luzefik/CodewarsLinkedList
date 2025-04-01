"""
Task

Create a function stringify which accepts an argument list / $list and returns a string representation of the list.
The string representation of the list starts with the value of the current Node, specified by its data / $data / Data property,
followed by a whitespace character, an arrow and another whitespace character (" -> "),
followed by the rest of the list. The end of the string representation of a list must always end with
null / NULL / None / nil / nullptr / null() ( all caps or all lowercase depending on the language you are undertaking this Kata in ).
For example, given the following list:

https://www.codewars.com/kata/582c297e56373f0426000098/solutions/python

def stringify(list):
    return 'None' if list == None else str(list.data) + ' -> ' + stringify(list.next)
"""

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    result = ''
    if node is None:
        print(None)
        result += "None"
        return result
    else:
        probe = node
        while probe:
            if probe.next is not None:
                print(probe.data, end=" -> ")
                result += f'{probe.data} -> '
            else:
                print(f"{probe.data} -> None")
                result += f"{probe.data} -> None"
            probe = probe.next
    return result

stringify(Node(0, Node(1, Node(2, Node(3)))))