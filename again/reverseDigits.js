// runtime O(Math.ceil(Math.log10(n)))
//
const reverseDigits = n => {
    const a = [];

    const isNegative = n < 0;

    if (isNegative) {
        n *= -1;
    }

    do {
        a.push(n % 10);
    } while (n = n / 10 >> 0);

    let reversed = a.join('');

    if (isNegative) {
        reversed = -reversed;
    }

    return (reversed < -(2 ** 31)) || (reversed > 2 ** 31) ?
        0 :
        reversed;
};

console.log(
    reverseDigits(-321)
);

