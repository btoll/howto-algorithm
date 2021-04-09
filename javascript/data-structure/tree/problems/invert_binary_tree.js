// https://leetcode.com/problems/invert-binary-tree/
//
//       4
//     /   \
//    2     7
//   / \   / \
//  1   3 6   9
//
//    becomes
//
//       4
//     /   \
//    7     2
//   / \   / \
//  9   6 3   1
//

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

const tree = new BT(4);

[2,7,1,3,6,9].forEach(tree.insert.bind(tree));

console.log('tree.root', tree.root);

const invert = tree => {
    const q = [tree.root];
    const v = [];

    while (q.length) {
        const node = q.pop();

        const tmp = node.left;
        node.left = node.right;
        node.right = tmp;

        if (node.left) q.unshift(node.left);
        if (node.right) q.unshift(node.right);
    }
};

invert(tree);

console.log();

console.log('inverted tree.root', tree.root);

