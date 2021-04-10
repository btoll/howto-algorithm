// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

//
//    3
//   / \
//  9  20
//    /  \
//   15   7
//

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

const buildTree = (preorder, inorder) => {
    if (inorder.length === 0) return null;

    const node = new TreeNode(preorder.shift());
    const pivotIndex = inorder.indexOf(node.val);

    node.left = buildTree(preorder, inorder.slice(0, pivotIndex));
    node.right = buildTree(preorder, inorder.slice(pivotIndex + 1));

    return node;
};

const preorder = [3,9,20,15,7];
const inorder = [9,3,15,20,7];

//const preorder = [1,2];
//const inorder = [1,2];

console.log(
    buildTree(preorder, inorder)
);

