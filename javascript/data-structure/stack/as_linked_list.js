const makeNode = v => ({
    val: v,
    next: null
});

class Stack {
    constructor() {
        this.head = null;
    }

    pop() {
        if (!this.head) {
            // Throw error?
        }

        const oldHead = this.head;
        this.head = oldHead.next;
        return oldHead.val;
    }

    push(item) {
        const node = makeNode(item);
        node.next = this.head;
        this.head = node;
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

const stack = new Stack();

console.log(stack.isEmpty());
stack.push(5);
stack.push(4);
stack.push(3);
console.log(stack.head);
stack.pop();
stack.pop();
stack.pop();
console.log(stack.head);

