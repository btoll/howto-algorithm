const nums = [1,2,2,2,3,4,5,5,6,6,7,7,7,7,8,9,9];
//const nums = [1,2,2,2,3,3,4];
console.log('original nums', nums);

const removeDuplicates = nums => {
    let k = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== nums[i + 1]) {
            nums[k++] = nums[i];
        }
    }

    return nums.slice(0, k);;
};

console.log(' removed nums', removeDuplicates(nums));

