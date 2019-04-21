const makeNode = v => ({
    val: v,
    next: null
});

const add = (head, v) => {
    if (!head) return makeNode(v);

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

const result = sum => ({
    val: sum % 10,
    carry: sum > 9 ? 1 : 0
});

const sumLists = (l1, l2) => {
    let carry = 0;
    let head;

    while (l1 && l2) {
        const res = result(l1.val + l2.val + carry);
        carry = res.carry;

        if (!head) head = add(null, res.val);
        else add(head, res.val);

        l1 = l1.next;
        l2 = l2.next;
    }

    while (l1) {
        const res = result(l1.val + carry);
        carry = res.carry;
        add(head, res.val);
        l1 = l1.next;
    }

    while (l2) {
        const res = result(l2.val + carry);
        carry = res.carry;
        add(head, res.val);
        l2 = l2.next;
    }

    return head;
};

const head1 = makeNode(7);
add(head1, 1);
add(head1, 6);

const head2 = makeNode(5);
add(head2, 9);
add(head2, 2);

//console.log(list(head1));
//console.log(list(head2));
const head3 = sumLists(head1, head2);
console.log(list(head3));

