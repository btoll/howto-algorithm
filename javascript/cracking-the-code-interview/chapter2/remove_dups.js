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

// One pass O(n).
//const removeDups = head => {
//    const cache = {};
//    let node = head;
//    let prev = null;
//
//    while (node) {
//        if (!cache[node.val]) {
//            cache[node.val] = 1;
//            prev = node;
//        } else {
//            prev.next = node.next;
//        }
//
//        node = node.next;
//    }
//
//    return head;
//};

// Two pointers O(n^2).
const removeDups = head => {
    let current = head;

    while (current) {
        let runner = current;

        while (runner.next) {
            if (current.val === runner.next.val) runner.next = runner.next.next;
            else runner = runner.next;
        }

        current = current.next;
    }

    return head;
};

let head = makeNode(1);

add(head, 6);
add(head, 1);
add(head, 1);
add(head, 3);
add(head, 2);
add(head, 2);
add(head, 2);
add(head, 5);
add(head, 3);
add(head, 3);
add(head, 1);
add(head, 2);
add(head, 2);
add(head, 3);
add(head, 1);
add(head, 1);
add(head, 1);
add(head, 1);
add(head, 1);
add(head, 3);
add(head, 5);
add(head, 4);
add(head, 4);
add(head, 1);

list(head);
head = removeDups(head);
console.log();
list(head);

