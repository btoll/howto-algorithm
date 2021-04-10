const powerOfTwo = n =>
    (n & (n - 1)) === 0;

for (let i = 1; i < 100; i++) {
    if (powerOfTwo(i)) console.log(i);
}

