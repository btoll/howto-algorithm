from LinkedList import LinkedList, Node


l_list = LinkedList(1)
for n in range(2, 7):
    l_list.add(n)



# Recursive
def swap_pairs(head):
    if not head or not head.next:
        return head

    first_node = head
    second_node = head.next

    # Unlink the 2nd...
    first_node.next = swap_pairs(second_node.next)
    # And swap it before the 1st.
    second_node.next = first_node

    # Return new HEAD.
    return second_node


# Iterative
def swap_pairs(head):
    head = head
    dummy = Node(-1)
    dummy.next = head
    prev_node = dummy

    while head and head.next:
        first_node = head
        second_node = head.next

        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev_node = first_node
        head = first_node.next
    return dummy.next


#print(l_list.get_head().next.next.next.value)
l_list.head = swap_pairs(l_list.head)
l_list.print()

#def swap_pairs(arr, start, end):
#    if start >= len(arr):
#        return arr
#
#    arr[end], arr[start] = arr[start], arr[end]
#    return swap_pairs(arr, start + 2, end + 2)
#
#
#def reverse_arr(arr, start, end):
#    if start > end:
#        return arr
#
#    arr[end], arr[start] = arr[start], arr[end]
#    return "".join(reverse_arr(arr, start + 1, end - 1))
#
#
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(swap_pairs(arr, 0, 1))
#string = "benissimo"
#l = list(string)
#print(reverse_arr(l, 0, len(l) - 1))
