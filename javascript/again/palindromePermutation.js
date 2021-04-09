const palindromePermutation = s => {
    s = s.replace(/\s/g, '').toLowerCase();

    const a = new Array(26);

    for (let i = 0; i < s.length; i++) {
        const ch = 'z'.charCodeAt() - s[i].charCodeAt();

        if (a[ch] === undefined) {
            a[ch] = 1;
        } else {
            a[ch]++;
        }
    }

    const canHaveOne = s.length % 2 === 1;
    let j = 0;

    for (let i = 0; i < a.length; i++) {
        const isOdd = a[i] % 2 === 1;
        if (!canHaveOne && isOdd) {
            return false;
        } else if (canHaveOne && isOdd) {
            if (j === 1) return false;
            else j = 1;
        }
    }

    return true;
};

console.log(
    palindromePermutation('aco catt')
);

