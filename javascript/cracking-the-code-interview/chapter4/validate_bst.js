function BT(v) {
    this.root = this.node(v);
}

BT.prototype.node = v => ({
    val: v,
    left: null,
    right: null
});

BT.prototype.max = function (node = this.root, max = 0) {
//    if (!node) return max;
//
//    max = this.max(node.left, max);
//    max = Math.max(max, node.val);
//    max = this.max(node.right, max);
//
//    return max;
    let s = [node];

    while (s.length) {
        const n = s.pop();

        max = Math.max(max, n.val);

        if (n.left) s.push(n.left);
        if (n.right) s.push(n.right);
    }

    return max;
};

BT.prototype.min = function (node = this.root, min = this.root.val) {
    if (!node) return min;

    min = this.min(node.left, min);
    min = Math.min(min, node.val);
    min = this.min(node.right, min);

    return min;
};

BT.prototype.insert = function (v) {
    let node = this.root;

    while (node) {
        if (v < node.val) {
            if (!node.left) return node.left = this.node(v);
            node = node.left;
        } else {
            if (!node.right) return node.right = this.node(v);
            node = node.right;
        }
    }
};

const tree = new BT(50);

tree.insert(100);
tree.insert(75);
tree.insert(25);
tree.insert(90);
tree.insert(95);
tree.insert(60);
tree.insert(10);

/*
const validateBST = (node, v = []) => {
    if (!node) return v;

    validateBST(node.left, v);
    v.push(node.val);
    validateBST(node.right, v);

    return v;
};
*/

/*
const checkBST = () => {
    const nodes = validateBST(tree.root);

    for (let i = 0; i < nodes.length - 1; i++) {
        if (nodes[i] > nodes[i + 1]) return false;
    }

    return true;
};
*/

const checkBST = (node, last = -1) => {
    if (!node) return;

    checkBST(node.left, node.val);
    console.log(node.val, last);
    checkBST(node.right, node.val);
};

//const checkBST = tree =>
//    tree.max(tree.left) < tree.root.val < tree.min(tree.right);

console.log(checkBST(tree.root));

