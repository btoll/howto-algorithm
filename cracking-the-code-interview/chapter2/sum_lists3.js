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

/*
const sumListReversed = head => {
    const a = [head.val];

    while (head.next) {
        head = head.next;
        a.push(head.val);
    }

    return a.reduce((acc, curr, p) => {
        acc += curr * 10**p;
        return acc;
    }, 0);
};
*/

const sumList = head => {
    const a = [head.val];

    while (head.next) {
        head = head.next;
        a.push(head.val);
    }

    return a.reduce((acc, curr, p) => {
        acc += curr * (100 / 10**p);
        return acc;
    }, 0);
};

/*
const reverseSummedList = sum => {
    const head = makeNode(sum % 10 >> 0);

    sum /= 10;
    while (sum > 1) {
        add(head, sum % 10 >> 0);
        sum /= 10;
    }

    return head;
};
*/

const forwardSummedList = sum => {
    let nl = Math.log10(sum) >> 0;
    const head = makeNode(sum / (10 ** nl) >> 0);
    sum %= 10 ** nl--;

    while (sum > 1) {
        add(head, sum / (10 ** nl) >> 0);
        sum %= 10 ** nl--;
    }

    return head;
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
//console.log();
//console.log('sumList(head1)', sumList(head1));
//console.log('sumList(head2)', sumList(head2));
//console.log(sumList(head1) + sumList(head2));
//console.log();

//const head3 = reverseSummedList(sumListReversed(head1) + sumListReversed(head2));
const head3 = forwardSummedList(sumList(head1) + sumList(head2));
list(head3);

