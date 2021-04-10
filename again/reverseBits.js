const reverseBits = n => {
    const bits = [];

    do {
        bits.push(n % 2);
    } while (n = n / 2 >> 0);

    return bits.reverse().join('');
};

console.log(
    reverseBits(1124)
);

