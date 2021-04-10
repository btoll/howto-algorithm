const makeNode = v => ({
    val: v,
    next: null
});

const add = (head, v) => {
    let node = head;

    while (node.next) {
        node = node.next;
    }

    const n = makeNode(v)
    node.next = n;

    return n;
};

const list = node => {
    if (!node) return;
    console.log(node.val);
    list(node.next);
};

const result = (node, length) => ({
    tail: node,
    length
});

const runner = list => {
    let len = 1;

    while (list.next) {
        list = list.next;
        len++;
    }

    return result(list, len);
};

const moveToKth = (node, length) => {
    // "Chop off" the longer list's first nodes so the lengths of both lists are equal.
    while (length && node) {
        node = node.next;
        length--;
    }

    return node;
};

const intersection = (l1, l2) => {
    let node1 = runner(l1);
    let node2 = runner(l2);

    // If they intersect at any point, the last nodes should be refs to each other!
    if (node1.tail !== node2.tail) return false;

    let [longer, shorter] = node1.length < node2.length ? [l2, l1] : [l1, l2];
    longer = moveToKth(longer, Math.abs(node1.length - node2.length));

    while (longer !== shorter) {
        longer = longer.next;
        shorter = shorter.next;
    }

    // Return either one.
    return longer;
};

const head1 = makeNode(7);
add(head1, 1);
add(head1, 6);
add(head1, 3);
add(head1, 11);
const n8 = add(head1, 8);
const n0 = add(head1, 0);
const n10 = add(head1, 10);

const head2 = makeNode(5);
add(head2, 9);
const n2 = add(head2, 2);
//add(head2, 12);
//add(head2, 13);
//add(head2, 14);
n2.next = n8;

//console.log(list(head1));
//console.log();
//console.log(list(head2));

console.log(intersection(head1, head2));

