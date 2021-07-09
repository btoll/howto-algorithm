import ipdb


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle(head):
    if not head:
        return False

    slow = head
    fast = head.next

#    while fast and fast.next:
    while slow is not fast:
        #        if slow is fast:
        if fast is None or fast.next is None:
            #            return True
            return False
        slow = slow.next
        # Make sure that the fast node is at least two nodes ahead.
        fast = fast.next.next
#    return False
    return True


# Return True if there's a cycle.
def cycle(head):
    c = {head: True}
    head = head.next
    while head:
        if head in c:
            return True
        c[head] = True
        head = head.next
    return False


# Return the node that is linked to by `tail.next`.
def cycle2(head):
    visited = set()
    head = head.next
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next
    return None

nums = [3, 2, 0, -4]
#nums = [3]

dummy = Node(-1)
temphead = dummy
for num in nums:
    dummy.next = Node(num)
    dummy = dummy.next

# Create the new head.
head = temphead.next
temphead.next = None

# Create the cycle.
dummy.next = head.next

#print(head.next.next.next.next.next.next.value)
print(cycle(head))
print(cycle2(head).value)
