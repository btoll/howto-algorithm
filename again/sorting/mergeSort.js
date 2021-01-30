const merge = (a, p, q, r) => {
    const low = a.slice(p, q);
    const high = a.slice(q, r);

    let k = p;
    let i = 0;
    let j = 0;

    while (i < low.length && j < high.length) {
        if (low[i] < high[j]) {
            a[k++] = low[i++];
        } else {
            a[k++] = high[j++];
        }
    }

    while (i < low.length) {
        a[k++] = low[i++];
    }

    while (j < high.length) {
        a[k++] = high[j++];
    }
};

const mergeSort = (a, p, r) => {
    const q = p + r >> 1;

    if (p === q) {
        return [];
    }

    mergeSort(a, p, q);
    mergeSort(a, q, r);
    merge(a, p, q, r);
};

const nums = [-100, 0, 75, -25, 50, -75, -50, 100, 25];
//const nums = [50, 40, 30, 20, 10];
//const nums = [50, 40, 30];

console.log('nums', nums);
mergeSort(nums, 0, nums.length);
console.log('nums', nums);

