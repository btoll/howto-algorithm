// Each new term in the Fibonacci sequence is generated by adding the previous two terms.
// By starting with 1 and 2, the first 10 terms will be:
//
//      1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.
//
//
const fibonacci = (() => {
    const cache = {};

    return n => {
        if (n <= 2) {
            return n;
        }

        return !cache[n] ?
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) :
            cache[n];
    };
})();

let k = 0;

// Simply loop and add the even terms until we get a value that is greater than the target (4 million).
for (let i = 1, j = 0; j < 4000000; i++, j = fibonacci(i)) {
    if (j % 2 === 0) {
        k += j;
    }
}

console.log(k);

