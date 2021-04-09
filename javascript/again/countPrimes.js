const countPrimes = n => {
    let cnt = 0;
    const array = [];

    for(let i = 2; i < n; i++) {
        if (array[i]) continue;
        else cnt++;

        for(let j = i + i; j <= n; j += i) {
            array[j] = true;
        }
    }

    return cnt;
};

console.log(
    countPrimes(16)
);

