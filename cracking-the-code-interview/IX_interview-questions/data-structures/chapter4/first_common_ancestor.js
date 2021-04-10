function BT(v) {
    this.root = this.node(v);
}

BT.prototype.node = v => ({
    val: v,
    left: null,
    right: null
});

BT.prototype.covers = function (parent, node) {
    if (!parent) return false;
    if (parent === node) return true;
    return this.covers(parent.left, node) || this.covers(parent.right, node);
};

BT.prototype.find = function (v) {
    const q = [this.root];

    while (q.length) {
        const node = q.pop();

        if (node.val === v) return node;

        if (node.left) q.push(node.left);
        if (node.right) q.push(node.right);
    }

    return -1;
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

const firstCommonAncestor = function (p, q, node = this.root) {
    if (!p || !q || !node) return node;

    const pOnLeft = this.covers(node.left, p);
    const qOnLeft = this.covers(node.left, q);

    if (pOnLeft !== qOnLeft) return node;
    return firstCommonAncestor.call(this, p, q, pOnLeft ? node.left : node.right);
};

const tree = new BT(1);

for (let i = 2; i < 16; i++) {
    tree.insert(i);
}

//console.log('tree', tree);

console.log(firstCommonAncestor.call(tree, tree.find(9), tree.find(11)));

