// Calculate the nth fibonacci number in the sequence.
const naiveFib = n => {
    if (n < 2) {
        return n;
    }

    return naiveFib(n - 2) + naiveFib(n - 1);
};

console.log(
    naiveFib(4)
);

