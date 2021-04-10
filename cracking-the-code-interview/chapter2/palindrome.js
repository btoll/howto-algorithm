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

const list = head => {
    let node = head;

    while (node) {
        console.log(node.val);
        node = node.next;
    }
};

/*
const palindrome = head => {
    const arr = [head.val];

    while (head.next) {
        head = head.next;
        arr.push(head.val);
    }

    for (let i = 0, j = arr.length - 1; i < j; i++, j--) {
        if (arr[i] !== arr[j]) return false;
    }

    return true;
};
*/

const palindrome = head => {
    let curr = head;
    const arr = [];

    while (curr) {
        arr.push(curr.val);
        curr = curr.next;
    }

    curr = head;

    for (let i = 0, len = arr.length >> 1; i <= len; i++) {
        if (curr.val !== arr.pop()) return false;
        curr = curr.next;
    }

    return true;
};

let head = makeNode('r');
add(head, 'a');
add(head, 'c');
add(head, 'e');
add(head, 'e');
add(head, 'c');
add(head, 'a');
add(head, 'r');

console.log(palindrome(head));

