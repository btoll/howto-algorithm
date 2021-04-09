const makeNode = v => ({
    val: v,
    next: null
});

class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    pop() {
        if (!this.head) {
            // Throw error?
        }

        const oldHead = this.head;
        this.head = oldHead.next;

        if (!this.head) this.tail = null;

        return oldHead.val;
    }

    push(item) {
        const node = makeNode(item);

        if (this.tail) this.tail.next = node;
        this.tail = node;
        if (!this.head) this.head = node;
    }

    peek() {
        if (this.head) {
            return this.head.val;
        }
    }

    isEmpty() {
        return !this.head;
    }
}

const q = new Queue();

q.push(42);
q.push(12);
q.push(25);

console.log(q);

q.pop();
q.pop();
q.pop();

console.log(q);

