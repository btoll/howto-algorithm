from LinkedList import Node


# Iterative
def merge_two_lists(l1, l2):
    l3 = Node(None)
    l3head = l3

    while l1 and l2:
        if l1.value < l2.value:
            l3.next = l1
            l1 = l1.next
        else:
            l3.next = l2
            l2 = l2.next
        l3 = l3.next

    l3.next = l1 or l2
    return l3head.next


# Recursive
def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.value < l2.value:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l2.next, l1)
        return l2


#l1 = [1, 2, 4]
#l2 = [1, 3, 4]
#l1 = LinkedList(1)
#l1.add(2)
#l1.add(4)
#
#l2 = LinkedList(1)
#l2.add(3)
#l2.add(4)

#l3 = merge_two_lists(l1.head, l2.head)

l1 = Node(0)
l1.next = Node(1)
l1.next.next = Node(1)
l1.next.next.next = Node(2)
l1.next.next.next.next = Node(4)
l1.next.next.next.next.next = Node(8)

l2 = Node(1)
l2.next = Node(3)
l2.next.next = Node(4)
l2.next.next.next = Node(5)
l2.next.next.next.next = Node(5)

l3 = merge_two_lists(l1, l2)

node = l3

while node:
    print(node.value)
    node = node.next
