class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicates(head):
    if not head:
        return None

    prev = Node(None)
    current = head

    while current:
        if current.value == prev.value:
            prev.next = current.next
        prev, current = current, current.next
    return head


def remove_duplicates(head):
    if not head:
        return None

    current = head
#    while current.next:
#        if current.value == current.next.value:
#            if not current.next.next:
#                current.next = None
#                break
#            current.next = current.next.next
#        current = current.next
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        current = current.next
    return head


nums = [1, 1, 2, 3, 3]
dummy = Node(-1)
temphead = dummy
for num in nums:
    dummy.next = Node(num)
    dummy = dummy.next

# Create the new head.
head = temphead.next
temphead.next = None

head = remove_duplicates(head)

while head:
    print(head.value)
    head = head.next
