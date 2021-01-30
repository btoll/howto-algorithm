const matrix = [
    [ 0, 0, 0, 0, 0],
    [ 0, 1, 1, 1, 0],
    [ 0, 0, 1, 0, 0],
    [ 0, 1, 1, 1, 0],
    [ 0, 0, 0, 0, 0]
];

const rotateMatrix = matrix => {
    const n = matrix.length;

    for (let layer = 0; layer < n / 2 >> 0; layer++) {
        const first = layer;
        const last = n - 1 - layer;

        console.log('first', first);
        console.log('last', last);

        for (let i = first; i < last; i++) {
            const offset = i - first;
            const top = matrix[first][i]; // save top;

            // left -> top
            matrix[first][i] = matrix[last - offset][first];

            // bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset];

            // right -> bottom
            matrix[last][last - offset] = matrix[i][last];

            // top -> right
            matrix[i][last] = top; // right <- saved top
        }
    }

    return matrix;
};

console.log(matrix);
console.log();
console.log(rotateMatrix(matrix));

