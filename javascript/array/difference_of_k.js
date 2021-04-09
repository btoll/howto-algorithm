const differenceOfK = (nums, k) => {
    let n = 0;

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (i === j) continue;
            if (Math.abs(nums[i] - nums[j]) === k) n++;
        }
    }

    return n / 2;
};

/*
const differenceOfK = (nums, k) => {
    const set = new Set();
    let x = 0;

    for (let n of nums) {
        if (!set.has(n)) {
            set.add(n);
        }

        if (set.has(Math.abs(k - n)) || set.has(Math.abs(k + n))) {
            x++;
        }
    }

    return x;
};
*/

const nums = [1, 7, 5, 9, 2, 12, 3];

console.log(differenceOfK(nums, 2));

