const merge = (nums, p, q, r) => {
    const low = nums.slice(p, q);
    const high = nums.slice(q, r);
    let i = 0;
    let j = 0;
    let k = p;

    while (i < low.length && j < high.length) {
        if (low[i] < high[j]) {
            nums[k++] = low[i++];
        } else {
            nums[k++] = high[j++];
        }
    }

    while (i < low.length) {
        nums[k++] = low[i++];
    }

    while (j < high.length) {
        nums[k++] = high[j++];
    }

    return nums;
};

const mergeSort = (nums, p, r) => {
    const q = (p + r) >> 1;
    if (p === q) return [];

    mergeSort(nums, p, q);
    mergeSort(nums, q, r);
    return merge(nums, p, q, r);
};

const nums = [-100, 0, 75, -25, 50, -75, -50, 100, 25];
console.log(mergeSort(nums, 0, nums.length));

