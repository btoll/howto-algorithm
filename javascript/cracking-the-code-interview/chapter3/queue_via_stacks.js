class Queue {
    constructor(...items) {
        this.enq = items || [];
        this.deq = [];
    }

    enqueue(item) {
        if (!this.enq.length) {
            while (this.deq.length) {
                this.enq.push(this.deq.pop());
            }
        }

        return this.enq.push(item);
    }

    dequeue(item) {
        if (!this.isEmpty()) {
            if (!this.deq.length) {
                while (this.enq.length) {
                    this.deq.push(this.enq.pop());
                }
            }

            return this.deq.pop();
        }

        return null;
    }

    peek() {
    }

    isEmpty() {
        return ![...this.enq, ...this.deq].length;
    }
}

const q = new Queue(5, 6, 7, -2);
console.log(q);
q.enqueue(42);
console.log(q.isEmpty());
console.log(q);
console.log(q.dequeue());

