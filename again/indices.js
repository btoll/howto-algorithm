/*
const indices = (a, n) => {
    const nums = [];

    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < a.length; j++) {
            if (j != i && (a[j] + a[i] === n)) {
                nums.push(j);
            }
        }
    }

    return nums.sort();
};
*/

const indices = (a, n) => {
    const m = {};
    const nums = [];

    for (let i = 0; i < a.length; i++) {
        const key = n - a[i];
        const res = m[key];

        if (!res) {
            m[a[i]] = i;
        } else {
            nums.push(res, i);
        }
    }

    return nums;
};

console.log(indices([2, 7, 9, 11, 15], 22));

