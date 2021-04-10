//
//              __ 100 __
//             /         \
//         50              150
//       /    \          /     \
//     25      75      125     175
//    /  \    /  \    /   \
//  15   30 110 130  170   200
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

    const queue = [this.root];

    while (queue.length) {
        const node = queue.pop();

        if (node.left) {
            queue.unshift(node.left);
        } else {
            return node.left = this.node(v);
        }

        if (node.right) {
            queue.unshift(node.right);
        } else {
            return node.right = this.node(v);
        }
    }
};

BST.prototype.print = function (node = this.root) {
    const queue = [this.root];

    while (queue.length) {
        const node = queue.pop();

        console.log(node.val);

        if (node.left) {
            queue.unshift(node.left);
        }

        if (node.right) {
            queue.unshift(node.right);
        }
    }
};

const tree = new BST(100);

[50, 150, 25, 75, 125, 175, 15, 30, 110, 130, 170, 200].forEach(
    tree.insert.bind(tree)
);

//console.log('tree', tree);
//console.log('tree.insert', tree.insert(400));
console.log('tree.insert', tree.insert(666));
console.log('tree.print', tree.print());
//console.log('height -> left', tree.height(tree.root.left));
//console.log('height -> right', tree.height(tree.root.right));
//console.log(tree.preorder());
//let node = tree.root;
//while (node) {
//    console.log(node.val);
//    node = node.right;
//}

