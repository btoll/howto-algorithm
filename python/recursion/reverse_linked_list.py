from LinkedList import LinkedList, Node


l_list = LinkedList(1)
for n in range(2, 7):
    l_list.add(n)

l_list.print()
print()


#def reverse_linked_list(head):
#    prev_node = head
#    curr_node = head.next
#
#    while curr_node:
#        next_node = curr_node.next   # Remember the next node.
#        curr_node.next = prev_node   # Swap the two.  None, the first time round.
#        prev_node = curr_node        # Used in the next iteration.
#        curr_node = next_node        # Move to next node.
#
#    return prev_node
#
#
#head = reverse_linked_list(l_list.get_head())
#print(head.next.next.next.next.next.next.next.value)


def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev

l_list.head = reverse_linked_list(l_list.get_head())
l_list.print()
