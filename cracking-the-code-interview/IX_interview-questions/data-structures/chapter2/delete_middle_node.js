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

const find = (head, v) => {
    let node = head;

    while (node) {
        if (node.val === v) {
            return node;
        }

        node = node.next;
    }

    return null;
};

const list = head => {
    let node = head;

    while (node) {
        console.log(node.val);
        node = node.next;
    }
};

/*
const deleteMiddleNode = head => {
    let tortoise = head;
    let hare = head;
    let prev = null;

    while (tortoise.next && hare.next) {
        prev = tortoise;
        tortoise = tortoise.next;
        hare = hare.next;
        if (hare.next) hare = hare.next;
    }

    prev.next = tortoise.next;
    return head;
};
*/

// Note that it's not possible to delete the last node using this method.
// You can mark it as a dummy, but that's about it, yo.
const deleteMiddleNode = node => {
    if (!node || !node.next) return false;

    node.val = node.next.val;
    node.next = node.next.next;
    return true;
};

let head = makeNode(1);

add(head, 2);
add(head, 3);
add(head, 4);
add(head, 5);
add(head, 6);
add(head, 7);
add(head, 8);
add(head, 9);
add(head, 10);

deleteMiddleNode(find(head, 3));

list(head);

