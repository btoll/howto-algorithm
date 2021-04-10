const ROWS = 5;
const COLS = 5;

const matrix = [
    [ 1, 1, 1, 1, 1 ],
    [ 1, 1, 0, 0, 1 ],
    [ 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1 ],
    [ 0, 1, 1, 1, 1 ]
];

const zeroMatrix = m => {
    const pair = [];

    for (let i = 0; i < m.length; i++) {
        for (let j = 0; j < m.length; j++) {
            if (m[i][j] === 0) {
                pair.push([i, j]);
            }
        }
    }

    pair.forEach(([row, col]) => {
        matrix[row] = matrix[row].map(v => 0);

        for (let k = 0; k < COLS; k++) {
            matrix[k][col] = 0;
        }
    });

    return m;
};

console.log(
    zeroMatrix(matrix)
);

