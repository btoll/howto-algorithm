// This solution is close.
/*
const removeDuplicates = a => {
    let j = 0;
    for (let i = 1; i < a.length; i++) {
        let k = i;

        while (a[k] <= a[i - 1]) {
            k++;
        }

        const tmp = a[i - 1];
        a[i] = a[k];
        a[k] = tmp;
        j++;
    }

    return a;
};
*/

const removeDuplicates = a => {
    let i = 0;

    for (let j = 1; j < a.length; j++) {
        if (a[j] != a[i]) {
            i++;
            a[i] = a[j];
        }
    }

    return i + 1;
};

console.log(
//    removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
);

