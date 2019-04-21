// Build a binary tree from an inorder array.

const inorder = [1,2,3,4,5,6,7,8,9];

const makeNode = v => ({
    val: v,
    left: null,
    right: null
});

const buildTree_inorder = v => {
    if (!v.length) return null;

    const q = v.length >> 1;
    const node = makeNode(v[q]);

    node.left = buildTree_inorder(v.slice(0, q));
    node.right = buildTree_inorder(v.slice(q + 1));

    return node;
};

console.log(buildTree_inorder(inorder).left);

