const insert = (nums, i) => {
    const key = nums[i];

    while (key < nums[i - 1]) {
        nums[i] = nums[(i--) - 1];
    }

    nums[i] = key;
};

const insertionSort = nums => {
    for (let i = 1; i < nums.length; i++) {
        insert(nums, i);
    }

    return nums;
};

const nums = [-100, 0, 75, -25, 50, -75, -50, 100, 25];
console.log(insertionSort(nums));

