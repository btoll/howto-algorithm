const makeNode = v => ({
    val: v,
    next: null
});

const add = (head, v) => {
    let node = head;

    while (node.next) {
        node = node.next;
    }

    node.next = makeNode(v);
};

/*
const list = head => {
    let node = head;

    while (node) {
        console.log(node.val);
        node = node.next;
    }
};
*/

const list = node => {
    if (!node) return;
    console.log(node.val);
    list(node.next);
};

const addLists = (l1, l2, carry = 0) => {
    if (!l1 && !l2 && !carry) return null;

    const node = makeNode();
    let value = carry;

    if (l1) value += l1.val;
    if (l2) value += l2.val;

    node.val = value % 10;

    if (l1 || l2) {
        const next = addLists(
            !l1 ? null : l1.next,
            !l2 ? null : l2.next,
            value > 9 ? 1 : 0
        );

        node.next = next;
    }

    return node;
};

const head1 = makeNode(7);
add(head1, 1);
add(head1, 6);

const head2 = makeNode(5);
add(head2, 9);
add(head2, 2);

//list(head1);
//console.log();
//list(head2);

console.log(addLists(head1, head2));

