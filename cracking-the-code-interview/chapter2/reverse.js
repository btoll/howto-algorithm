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

    node.next = makeNode(v);
    return head;
};

const list = head => {
    let node = head;

    while (node) {
        console.log(node.val);
        node = node.next;
    }
};

const reverse = head => {
    let prev = null;
    let curr = head;
    let next = null;

    while (curr) {
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
};

let head = add(null, 1);
add(head, 2);
add(head, 3);
add(head, 4);
add(head, 5);
add(head, 6);
add(head, 7);
add(head, 8);
add(head, 9);

list(head);
console.log();
debugger;
list(reverse(head));

