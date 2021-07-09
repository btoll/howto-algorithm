import ipdb


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Iterative
def reverse(head):
    prev = None
    current = head

    while current:
        ipdb.set_trace()
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
#        prev, current.next, current = current, prev, current.next
    return prev


# Recursive
#def reverse(head):
#    pass


#nums = [1, 2, 3, 4, 5]
nums = [2, 3, 4]

dummy = Node(-1)
temphead = dummy
for num in nums:
    dummy.next = Node(num)
    dummy = dummy.next

# Create the new head.
head = temphead.next
temphead.next = None

head = reverse(head)

while head:
    print(head.value)
    head = head.next
