// Make array 1..100, inclusive.
const nums = [...Array(100).keys()].map(n => n + 1);

console.log('zero out', nums[51], nums[51] = 0);

const sum = nums.reduce((a, c) => a + c, 0)

// n(n + 1)          n^2 + n
// --------   --->   -------
//    2                 2
const gauss = (nums.length ** 2 + nums.length) / 2;

console.log('add numbers 1..100 (gauss)', gauss);
console.log('missing number =', gauss - sum);

