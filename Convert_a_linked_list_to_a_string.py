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