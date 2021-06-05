from LinkedList import LinkedList

import ipdb


# Note that this can't work with the tail node!
def delete_given_node(node):
    while node.next:
        prev = node
        node.value = node.next.value
        node = node.next
    try:
        prev.next = None
    except Exception:
        print("Unable to delete the tail node!")


l_list = LinkedList(1)
for i in range(2, 6):
    l_list.add(i)

l_list.print()
delete_given_node(l_list.get(5))
#l_list.delete(5)
print()
l_list.print()
