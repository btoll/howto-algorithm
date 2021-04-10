/*
const insertion = (N, M, start, end) => {
    const res = [];

    for (let i = N.length - 1, k = 0; i >= 0; i--, k++) {
        if (k === start) {
            let n = 0;

            while (start <= end) {
                res.push(M[M.length - 1 - (n++)]);
                start++;
                i--;
            }

            i++;
        } else {
            res.push(N[i]);
        }
    }

    return res.reverse().join('');
};
*/

const insertion = () {
};

/*
const btoi = s => {
    let res = 0;

    for (let i = s.length - 1, k = 0; i >= 0; i--) {
        if (s[i] === '1') res += 2 ** k;
        k++;
    }

    return res;
};
*/

const N = '10000000000';
const M = '10011';
const i = 2;
const j = 6;

// Output: 10001001100

console.log(insertion(N, M, i, j));
//console.log(btoi(M));

