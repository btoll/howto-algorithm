function BT(v) {
    this.root = this.node(v);
}

BT.prototype.node = v => ({
    val: v,
    left: null,
    right: null
});

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

BT.prototype.isBalanced = function (node = this.root) {
    return Math.abs(this.maxHeight(node.left) - this.minHeight(node.right)) < 2;
};

BT.prototype.inorder = function (node = this.root) {
    if (!node) return;

    console.log(node.val);

    this.inorder(node.left);
    this.inorder(node.right);
};

BT.prototype.minHeight = function (node = this.root) {
    if (!node) return -1;
    return 1 + Math.min(this.minHeight(node.left), this.minHeight(node.right));
};

BT.prototype.maxHeight = function (node = this.root) {
    if (!node) return -1;
    return 1 + Math.max(this.maxHeight(node.left), this.maxHeight(node.right));
};

const tree = new BT(1);

for (let i = 2; i < 16; i++) {
    tree.insert(i);
}

console.log(tree.isBalanced());

//console.log(tree.inorder(tree.root.left));
//console.log();
//console.log(tree.inorder(tree.root.right));

