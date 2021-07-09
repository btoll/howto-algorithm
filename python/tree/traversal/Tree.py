import ipdb


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, nodelist):
        self.nodes = nodelist[:]
        self.root = None
        self.make_tree()

    def display(self):
        queue = [self.root]
        visited = []

        while queue:
            node = queue.pop()
            visited.append(node.value)
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

        print("visited, BFS", visited)

    def get_height(self):
        length = len(self.nodes)
        i = 0

        # Constrain to at most 1024 nodes.
        while i < 10:
            if (2 ** i) > length:
                return i
            i += 1

    def get_root(self):
        return self.root

    def make_tree(self):
        # Root must call TreeNode, all other parents will already
        # have been instanced and can just be looked-up.
        self.nodes[0] = self.root = TreeNode(self.nodes[0])
        for i in range(len(self.nodes) // 2):
            parent = self.nodes[i]
            self.nodes[2*i+1] = parent.left = TreeNode(self.nodes[2*i+1])
            if 2*i+2 < len(self.nodes) and self.nodes[2*i+2] is not None:
                self.nodes[2*i+2] = parent.right = TreeNode(self.nodes[2*i+2])
