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

const partition = (head, k) => {
    let node = head;
    let low = null;
    let high = null;

    while (node) {
        if (node.val < k) low = add(low, node.val);
        else high = add(high, node.val);

        node = node.next;
    }

    if (!low) return high;
    if (!high) return low;

    node = low;

    while (node.next) {
        node = node.next;
    }

    node.next = high;
    return low;
};

let head = add(null, 8);

add(head, 6);
add(head, 9);
add(head, 7);
add(head, 3);
add(head, 2);
add(head, 5);
add(head, 4);
add(head, 1);

list(head);
console.log();
const low = partition(head, 50);
list(low);

