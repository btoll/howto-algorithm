const insertionSort = nums => {
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < nums[i - 1]) {
            let k = nums[i];
            let j = i - 1;
            // We've already compared this,
            // let's not compare it again.
            nums[i] = nums[j];

            while (k < nums[j - 1]) {
                nums[j] = nums[j - 1];
                j--;
            }

            nums[j] = k;
        }
    }

    return nums;
};

console.log(insertionSort([9,8,7,6,5,-9,4,0,3,2,1]));

