const swap = (nums, i, j) => {
    const tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
};

const partition = (nums, p, r) => {
    let low = p
    let k = p;
    let pivot = nums[r]; // Right-most element.

    while (low < r) {
        if (nums[low] <= pivot) {
            swap(nums, low, k++);
        }

        low++;
    }

    swap(nums, k, r);

    return k;
};

const quickSort = (nums, p, r) => {
    if (p >= r) return nums;

    const pivot = partition(nums, p, r);

    quickSort(nums, p, pivot - 1);
    quickSort(nums, pivot, r);

    return nums;
};

const a = [5,8,1,2,0,9,3,4,-83,7,17,5,6];
//const a = [9,3,4,7,5,6];

console.log('original unsorted array', a);
console.log('           sorted array', quickSort(a, 0, a.length - 1));

