// Recursive.
const fibonacci = n => {
    if (n < 2) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
};

// Memoized.
const fibonacci_memoized = (() => {
    const cache = new Map();

    return n => {
        if (n < 2) return n;

        if (cache.has(n)) {
            return cache.get(n);
        } else {
            const fib = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2);
            cache.set(n, fib);
            return fib;
        }
    };
})();

// Iterative.
const fibonacci2 = n => {
    if (n < 0) return 0;
    if (n === 0) return 0;
    if (n === 1) return 1;

    let a = 0;
    let b = 1;

    while (n > 0) {
        [a, b] = [a + b, a];
        n--;
    }

    return a;
};

/*
for (let i = 0; i < 50; i++) {
    console.log(fibonacci(i));
}
*/

//console.log();

for (let i = 0; i < 100; i++) {
    console.log(fibonacci_memoized(i));
}

//console.log();
//
//for (let i = 0; i < 30; i++) {
//    console.log(fibonacci2(i));
//}

