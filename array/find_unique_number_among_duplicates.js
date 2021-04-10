// Make array 1..20, duplicates (0, 0), (1, 1), (2, 2), etc.
const nums = [...Array(20).keys()].map((n, i) => {
    const v = n % 10;
    return v ? v : 10;
});

console.log('push on a unique number 17', nums.push(17));
console.log(`\nswap the last element to the middle (not necessary)\nbut show that it's not just using the last element\n`);

const q = nums.length >> 1;
const tmp = nums[nums.length - 1];

nums[nums.length - 1] = nums[q];
nums[q] = tmp;

console.log(
    'unique number =',
    nums.reduce((a, c) => a ^ c, 0)
);

