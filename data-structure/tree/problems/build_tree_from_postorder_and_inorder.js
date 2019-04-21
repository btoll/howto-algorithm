// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

//
//    3
//   / \
//  9  20
//    /  \
//   15   7
//

//
//    1
//     \
//      3
//     / \
//    2   4
//

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

const buildTree = (inorder, postorder) => {
    if (inorder.length === 0) return null;

    const node = new TreeNode(postorder[postorder.length - 1]);
    const pivotIndex = inorder.indexOf(node.val);

    node.left = buildTree(inorder.slice(0, pivotIndex), postorder.slice(0, pivotIndex));
    node.right = buildTree(inorder.slice(pivotIndex + 1), postorder.slice(pivotIndex, postorder.length - 1));

    return node;
};

//const postorder = [9,15,7,20,3];
//const inorder = [9,3,15,20,7];

//const postorder = [1,2];
//const inorder = [1,2];

const inorder = [1,2,3,4];
const postorder = [3,2,4,1];

console.log(
    buildTree(inorder, postorder)
);

