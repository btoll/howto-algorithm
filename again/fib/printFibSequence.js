const fib = (limit = 10) => {
    let n = 2;
    let a = 0;
    let b = 1;

    console.log(0);
    console.log(1);

    while (n < limit) {
        [b, a] = [a + b, b];
        console.log(b);
        n++;
    }
};

console.log(fib(30));

