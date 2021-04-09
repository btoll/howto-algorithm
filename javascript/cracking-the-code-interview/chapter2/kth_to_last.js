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

const kthToLast = (head, k) => {
    let tortoise = head;
    let hare = head;
    let i = 0;

    while (i < k) {
        if (!hare) return null;
        hare = hare.next;
        i++;
    }

    while (hare) {
        hare = hare.next;
        tortoise = tortoise.next;
    }

    return tortoise;
};

/*
const kthToLast = (node, k) => {
    if (!node) return 0;

    const index = kthToLast(node.next, k) + 1;
    if (k === index) console.log(node.val);
    return index;
};
*/

let head = makeNode(1);

add(head, 6);
add(head, 1);
add(head, 3);
add(head, 2);
add(head, 5);
add(head, 3);
//add(head, 1);
//add(head, 3);
//add(head, 1);
//add(head, 3);
//add(head, 5);
//add(head, 4);
add(head, 1);

console.log(kthToLast(head, 3));

