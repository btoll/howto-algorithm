class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def setup(head, pos):
    n1 = head
    n2 = head.next
    tail = head

    # Create the cycle.
    cycle_node = None
    while tail.next:
        if not pos:
            cycle_node = tail
        tail = tail.next
        pos -= 1
    if not cycle_node and pos == 0:
        tail.next = tail
    else:
        tail.next = cycle_node

    return n1, n2


# Using a Set to determine if the node has been seen before.
def has_cycle(head, pos):
    n1, _ = setup(head, pos)

    cache = set()
    while n1:
        if n1 in cache:
            return True
        cache.add(n1)
        n1 = n1.next
    return False


# Floyd's cycle finding algorithm (tortoise and hare).
def has_cycle(head, pos):
    n1, n2 = setup(head, pos)

    while n1 != n2:
        if not n2 or not n2.next:
            return False
        n1 = n1.next
        n2 = n2.next.next
    return True


head = [3, 2, 0, -4]
node = Node(3)
node.next = Node(2)
node.next.next = Node(0)
node.next.next.next = Node(-4)

print(has_cycle(node, 2))
