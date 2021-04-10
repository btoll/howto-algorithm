// https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

// inorder  = [9,3,15,20,7]
// preorder = [3,9,20,15,7]
//
//    3
//   / \
//  9  20
//    /  \
//   15   7
//

const treeNode = val => ({
    val: val,
    left: null,
    right: null
});

const buildTree = (pivot = 0, start = 0, end = inorder.length - 1) => {
    if (start > end) return;

    const n = preorder[pivot++];
    const node = treeNode(n);

    if (start === end) return node;

    const partition = inorder.indexOf(n);

    node.left = buildTree(pivot, start, partition - 1);
    node.right = buildTree(pivot, partition + 1, end);

    return node;
};

const inorder = [9,3,15,20,7];
const preorder = [3,9,20,15,7];

console.log(buildTree());

