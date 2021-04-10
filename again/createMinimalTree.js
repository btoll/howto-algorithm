/*
const foo = (a, p, q, r) => {
    console.log('a.slice(p, q)', a.slice(p, q));
    console.log('a.slice(q, r)', a.slice(q, r));
//    console.log('a, p, q, r', a, p, q, r);
};

const createMinimalTree = (a, p, r) => {
    if (p >= r) {
        return a;
    }

    const q = (p + r) / 2 >> 0;

    createMinimalTree(a, p, q);
    createMinimalTree(a, q, r - 1);

    return foo(a, p, q, r);

};
*/

function TreeNode(v) {
    this.value = v;
    this.left = null;
    this.right = null;
}

const createMinimalTree = (a, start, end) => {
    if (start > end) {
        return null;
    }

    const mid = (start + end) / 2 >> 0;

    const n = new TreeNode(a[mid]);

    n.left = createMinimalTree(a, start, mid - 1);
    n.right = createMinimalTree(a, mid + 1, end);

    return n;

};

const nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9];

console.log(
    createMinimalTree(nodes, 0, nodes.length)
);

