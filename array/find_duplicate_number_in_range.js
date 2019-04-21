// Make array 1..100, inclusive.
const nums = [...Array(100).keys()].map(n => n + 1);

console.log('push duplicate number 32 onto array', nums.push(32));
const sum = nums.reduce((a, c) => a + c, 0)

// n(n + 1)          n^2 + n
// --------   --->   -------
//    2                 2
const gauss = (100 ** 2 + 100) / 2;

console.log('add numbers 1..100 (gauss)', gauss);
console.log('duplicate number =', sum - gauss);

