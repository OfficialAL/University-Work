class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def merge_sorted_list(a, b):
    result = None

    if a is None:
        return b
    elif b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = merge_sorted_list(a.next, b)
    else:
        result = b
        result.next = merge_sorted_list(a, b.next)
    return result


a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)

b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

merged_list = merge_sorted_list(a, b)

temp = merged_list
print("Merged Link List is:")
while temp:
        print(temp.data, end=" ")
        temp = temp.next
