const makeNode = v => ({
    val: v,
    left: null,
    right: null
});

const minimalTree = (nodes, arr = [])  => {
    if (nodes.length < 1) return null;

    const q = nodes.length >> 1;
    const node = makeNode(nodes[q]);

    node.left = minimalTree(nodes.slice(0, q));
    node.right = minimalTree(nodes.slice(q + 1));

    return node;;
};

const nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const root = minimalTree(nodes);

console.log(root);

