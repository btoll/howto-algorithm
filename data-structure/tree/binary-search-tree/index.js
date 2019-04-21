//
//
//              __ 100 __
//             /         \
//         50              150
//       /    \          /     \
//     25      75      125     175
//    /  \           /    \   /   \
//  15   30        110   130 170  200
//
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

BST.prototype.has = function (v) {
    let node = this.root;

    while (node) {
        if (v === node.val) return node;
        else if (v < node.val) node = node.left;
        else node = node.right;
    }

    return null;
};

BST.prototype.height = function (node = this.root) {
    if (!node) return -1;
    return 1 + Math.max(this.height(node.left), this.height(node.right));
};

BST.prototype.insert = function (v) {
    let node = this.root;

    while (node) {
        if (v < node.val) {
            if (!node.left) return node.left = this.node(v);
            else node = node.left;
        } else {
            if (!node.right) return node.right = this.node(v);
            else node = node.right;
        }
    }
};

BST.prototype.remove = function (v) {
    let node = this.root;

    const remove = (node, v) => {
        if (!node) return null;

        if (v === node.val) {
            if (!node.left && !node.right) {
                return null;
            } else if (!node.left) {
                return node.right;
            } else if (!node.right) {
                return node.left;
            } else {
                let tmp = node.right;

                while (!tmp.left) {
                    tmp = tmp.left;
                }

                node.value = tmp.value;
                node.right = remove(node.right, tmp.value);
                return node;
            }
        } else if (v < node.val) {
            node.left = remove(node.left, v);
            return node;
        } else {
            node.right = remove(node.right, v);
            return node;
        }
    };

    remove(node, v);
};

BST.prototype.sum = function (node = this.root/*, n = 0*/) {
//    if (!node) return n;
//
//    n += node.val;
//    n = this.sum(node.left, n);
//    n = this.sum(node.right, n);
//
//    return n;
    if (!node) return 0;
    return this.sum(node.left) + node.val + this.sum(node.right);
};

/* ----------------------------------------------------------- */
/* ----------------------------------------------------------- */
/*                          Traversal                          */
/* ----------------------------------------------------------- */
/* ----------------------------------------------------------- */

BST.prototype.inorder = function (node = this.root/*, v = []*/) {
//    if (!node) return v;
//
//    this.inorder(node.left, v);
//    v.push(node.val);
//    this.inorder(node.right, v);
//
//    return v;
    if (!node) return [];

    const s = [];
    const v = [];
    let curr = node;

    while (curr || s.length) {
        while (curr) {
            s.push(curr);
            curr = curr.left;
        }

        curr = s.pop();
        v.push(curr.val);
        curr = curr.right;
    }

    return v;
};

BST.prototype.postorder = function (node = this.root/*, v = []*/) {
//    if (!node) return v;
//
//    this.postorder(node.left, v);
//    this.postorder(node.right, v);
//    v.push(node.val);
//
//    return v;
    if (!node) return [];

    let curr = node;
    const s = [node];
    const v = [];

    debugger;
//    while (curr || s.length) {
    while (s.length) {
//        while (curr) {
//            if (curr.right) s.push(curr.right);
//            if (curr.left) s.push(curr.left);
//            curr = curr.left;
//        }
//
//        curr = s.pop();
//        v.push(curr.val);
//        curr = curr.left;
        while (curr) {
            if (curr.right) s.push(curr.right);
            if (curr.left) s.push(curr.left);
            curr = curr.left;
        }

        curr = s.pop();
        console.log('got here', curr.val);
        v.push(curr.val);
        curr = curr.left;
    }

    return v;
};

BST.prototype.preorder = function (node = this.root/*, v = []*/) {
//    if (!node) return v;
//
//    v.push(node.val);
//    this.preorder(node.left, v);
//    this.preorder(node.right, v);
//
//    return v;
    if (!node) return [];

    const s = [node];
    const v = [];

    while (s.length) {
        const curr = s.pop();
        v.push(curr.val);

        if (curr.right) s.push(curr.right);
        if (curr.left) s.push(curr.left);
    }

    return v;
};

/* ----------------------------------------------------------- */
/* ----------------------------------------------------------- */

const tree = new BST(100);

tree.insert(150);
tree.insert(50);
tree.insert(25);
tree.insert(75);
//tree.insert(125);
//tree.insert(110);
//tree.insert(175);
//tree.insert(130);
//tree.insert(170);
//tree.insert(200);
//tree.insert(15);
//tree.insert(30);

//console.log(tree.has(15));
//tree.remove(150);
//console.log(tree.height());
//console.log(' preorder', tree.preorder());
//console.log();
console.log('  inorder', tree.inorder());
//console.log();
// postorder [ 15, 30, 25, 75, 50, 110, 130, 125, 170, 200, 175, 150, 100 ]
//console.log('preorder', tree.preorder());
console.log('sum', tree.sum());
//const s = [];
//s.push(tree.root);
//s.push(tree.root.right);
//s.push(tree.root.left);
//let n = s.pop();
//console.log(n.val);
//n = s.pop();
//console.log(n.val);
//n = s.pop();
//console.log(n.val);

