from Tree import Tree


#def is_uni(node, val=0):
#    if not node.left and not node.right:
#        return node.value == val
#
#    return is_uni(node.left, node.value) and is_uni(node.right, node.value)


# https://leetcode.com/problems/count-univalue-subtrees/discuss/1182525/Python-very-easy-to-understand-DFSBottom-up-Solution-using-Sets-O(n)-time
# print(is_uni(is_uni, tree.get_root()))
#def is_uni(self, root):
#    self.count = 0
#
#    def dfs(node, acc):
#        if not node:
#            return acc
#        left = dfs(node.left, acc)
#        right = dfs(node.right, acc)
#        print("left", left)
#        print("right", right)
#        acc = left.union(right)
#        acc.add(node.value)
#        self.count += (len(acc) == 1)
#
#        return acc
#
#    dfs(root, set())
#
#    return self.count

class Solution:
    def count_unival_subtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):
        # considered a valid subtree
        if node is None:
            return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.value),
                    self.is_valid_part(node.right, node.value)]):
            return False

#        print(node.value, val)

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.value == val


tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
#tree = Tree([1, 2, 3, 4, 5, 6, 7, 4, 4, 5, 5, 6, 6, 7, 7])
#tree = Tree([2, 2, 1, 2, 2])
print(Solution().count_unival_subtrees(tree.root))
