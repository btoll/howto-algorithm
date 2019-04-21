function BT(v) {
    this.root = this.node(v);
}

BT.prototype.node = v => ({
    val: v,
    left: null,
    right: null
});

// DFS
/*
BT.prototype.height = function (node = this.root) {
    const s = [node];

    while (s.length) {
        const node = s.pop();

        console.log(node.val);

        if (node.right) s.push(node.right);
        if (node.left) s.push(node.left);
    }
};
*/

BT.prototype.height = function (node = this.root) {
    if (!node) return -1;
    return 1 + Math.max(this.height(node.left), this.height(node.right));
};

BT.prototype.insert = function (v) {
    const q = [this.root];

    while (q.length) {
        let node = q.shift();

        if (!node.left) return node.left = this.node(v);
        if (!node.right) return node.right = this.node(v);

        q.push(node.left);
        q.push(node.right);
    }
};

BT.prototype.inorder = function (node = this.root, n = []) {
    if (!node) return;
    this.inorder(node.left, n);
    n.push(node.val);
    this.inorder(node.right, n);
    return n;
};

BT.prototype.postorder = function (node = this.root, n = []) {
    if (!node) return;
    this.postorder(node.left, n);
    this.postorder(node.right, n);
    n.push(node.val);
    return n;
};

BT.prototype.preorder = function (node = this.root, n = []) {
    if (!node) return;
    n.push(node.val);
    this.preorder(node.left, n);
    this.preorder(node.right, n);
    return n;
};

const tree = new BT(1);

for (let i = 2; i < 16; i++) {
    tree.insert(i);
}

//console.log(tree.height());

//console.log(tree);
//console.log(tree.root.left);
//console.log(tree.root.right);
//console.log(tree.inorder());

console.log(' preorder', tree.preorder());
console.log('  inorder', tree.inorder());
//console.log('postorder', tree.postorder());

const rootN = tree.preorder()[0];
const rootIndex = tree.inorder().indexOf(rootN);
const left = tree.inorder().slice(0, rootIndex);
const right = tree.inorder().slice(rootIndex + 1);
console.log('rootN', rootN);
console.log('left', left);
console.log('right', right);

