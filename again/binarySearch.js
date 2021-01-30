//const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];
//
//const binarySearch = (p, r, n) => {
//    if (p > r) {
//        return -1;
//    }
//
//    const q = (p + r) / 2 >> 0;
//
//    if (nums[q] == n) {
//        return q;
//    }
//
//    if (nums[q] > n) {
//        return binarySearch(p, q - 1, n);
//    } else {
//        return binarySearch(q + 1, r, n);
//    }
//};
//
//console.log(
//    binarySearch(0, nums.length - 1, 9)
//);

const binarySearch = (arr, n) => {
    let min = 0;
    let max = arr.length - 1;

    while (true) {
        const mid = (max + min) / 2 >> 0;

        if (max < min) {
            return -1;
        }

        if (arr[mid] === n) {
            return mid;
        }

        if (arr[mid] > n) {
            max = mid - 1;
        } else {
            min = mid + 1;
        }
    }
};

console.log(
    binarySearch(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        7
    )
);

