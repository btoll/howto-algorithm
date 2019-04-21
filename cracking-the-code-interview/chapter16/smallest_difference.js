/*
// Brute force, O(a*b).
const smallestDifference = (a1, a2) => {
    let min = Infinity;

    for (let i = 0; i < a1.length; i++) {
        for (let j = 0; j < a2.length; j++) {
            if (i == j) continue;
            min = Math.min(Math.abs(a1[i] - a2[j]), min);
        }
    }

    return min;
};
*/

const smallestDifference = (a1, a2) => {
    a1.sort((a, b) => a - b);
    a2.sort((a, b) => a - b);
    console.log('a1', a1);
    console.log('a2', a2);
};

console.log(smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]));

