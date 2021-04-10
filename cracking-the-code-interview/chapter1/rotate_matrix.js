const createMatrix = () => {
    const matrix = [];
    let rows = 4;
    let k = 1;

    for (let i = 0; i < rows; i++) {
        matrix[i] = [];

        for (let j = 0; j < rows; j++) {
            matrix[i][j] = k++;
        }
    }

    return matrix;
};

const rotateMatrix = matrix => {
    if (!matrix.length || matrix.length !== matrix[0].length) return false;

    const n = matrix.length;

    for (let layer = 0; layer < n >> 1; layer++) {
        let first = layer;
        let last = n - 1 - layer;

        for (let i = first; i < last; i++) {
            let offset = i - first;

            // Save top;
            let top = matrix[first][i];
            let left = matrix[last - offset][first];
            let right = matrix[i][last];
            let bottom = matrix[last][last - offset];

            // Left -> top.
            matrix[first][i] = left;

            // Bottom -> left.
            matrix[last - offset][first] = bottom;

            // Right -> bottom.
            matrix[last][last - offset] = right;

            // Top -> right.
            matrix[i][last] = top; // Right <- saved top.
        }
    }

    return true;
};

const matrix = createMatrix();

console.log('before');
console.log(matrix);
rotateMatrix(matrix);
console.log();
console.log('after');
console.log(matrix);

