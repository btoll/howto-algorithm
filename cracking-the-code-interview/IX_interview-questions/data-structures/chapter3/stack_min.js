// pop, push(item), peek, isEmpty

class Stack {
    constructor(...items) {
        this.stack = items || [];
        this.minimum = Math.min(...items);
    }

    pop() {
        const popped = this.stack.pop();
        this.minimum = Math.min(...this.stack);
        return popped;
    }

    push(...item) {
        this.minimum = Math.min(this.minimum, ...item);
        return this.stack.push(...item);
    }

    peek() {
        return this.stack[this.stack.length - 1];
    }

    isEmpty() {
        return !this.stack.length;
    }

    min() {
        return this.minimum;
    }
}

const stackMin = new Stack(5, 6, 7, -2);
console.log(stackMin.min());
stackMin.pop();
console.log(stackMin.min());
stackMin.push(99, -99, 50);
console.log(stackMin.min());

