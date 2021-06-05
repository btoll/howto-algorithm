function move(arr, i) {
    num = arr[i];
    prev = i - 1

    while (num < arr[prev]) {
        arr[i--] = arr[prev--];
    }

    arr[i] = num
}

function insertion(arr) {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) {
            move(arr, i);
        }
    }

    return arr;
}

def insertion(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            move(arr, i)
    return arr


//arr = [100, 0, 5, 0, -9, 4, 1, -100];
arr = [5, 0];
//console.log("start", arr);
console.log(insertion(arr));
