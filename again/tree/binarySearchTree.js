//
//              __ 100 __
//             /         \
//         50              150
//       /    \          /     \
//     25      75      125     175
//    /  \           /    \   /   \
//  15   30        110   130 170  200
//

function BST(v) {
    this.root = this.node(v);
}

BST.prototype = Object.create(null);

BST.prototype.node = function (v) {
    return {
        val: v,
        left: null,
        right: null
    };
};

BST.prototype.height = function (node = this.root) {
    if (!node) {
        return -1;
    }

    return 1 + Math.max(this.height(node.left), this.height(node.right));
};

BST.prototype.insert = function (v) {
    if (!v) {
        return null;
    }

    let node = this.root;

    while (node) {
        if (v <= node.val) {
            if (!node.left) {
                return node.left = this.node(v);
            } else {
                node = node.left;
            }
        } else {
            if (!node.right) {
                return node.right = this.node(v);
            } else {
                node = node.right;
            }
        }
    }
};

BST.prototype.preorder = function (node = this.root) {
    if (!node) {
        return;
    }

    console.log(node.val);
    this.preorder(node.left);
    this.preorder(node.right);
};

const tree = new BST(100);

[50, 150, 25, 75, 125, 175, 15, 30, 110, 130, 170, 200].forEach(
    tree.insert.bind(tree)
);

//console.log('tree', tree);
//console.log('height -> left', tree.height(tree.root.left));
//console.log('height -> right', tree.height(tree.root.right));
console.log(tree.preorder());
//let node = tree.root;
//while (node) {
//    console.log(node.val);
//    node = node.right;
//}

