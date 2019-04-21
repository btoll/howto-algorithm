const makeNode = v => ({
    val: v,
    next: null
});

const add = (head, v) => {
    let node = head;

    while (node.next) {
        node = node.next;
    }

    const n = makeNode(v);
    node.next = n;
    return n;
};

const list = node => {
    if (!node) return;

    console.log(node.val);
    list(node.next);
};

const head = makeNode('A');
const B = add(head, 'B');
const C = add(head, 'C');
const D = add(head, 'D');
const E = add(head, 'E');
const F = add(head, 'F');
const G = add(head, 'G');
const H = add(head, 'H');
H.next = E;

const loopDetection = head => {
    let tortoise = head;
    let hare = head;

    while (hare && hare.next) {
        tortoise = tortoise.next;
        hare = hare.next.next;
        if (tortoise === hare) return tortoise;
    }

    if (!hare || hare.next) return false;
};

console.log(loopDetection(head));

