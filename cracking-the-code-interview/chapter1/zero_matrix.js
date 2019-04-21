const makeMatrix = (col, row) => {
    const arr = [];

    for (let i = 0; i < row; i++) {
        arr.push(Array(col).fill(-1));
    }

    return arr;
};

const zeroMatrix = (col, row) => {
    const matrix = makeMatrix(col, row);

    matrix[3][2] = 0;
    console.log(matrix);
};

console.log(zeroMatrix(5, 5));

