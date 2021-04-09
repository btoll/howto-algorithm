const ROWS = 5;
const COLS = 5;

const matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
];

const visited = [];

for (let i = 0; i < ROWS; i++) {
    const row = [];

    for (let j = 0; j < COLS; j++) {
        row[j] = 0;
    }

    visited[i] = row;
}

const xNeighbors = [ -1, -1, -1, 0, 0, 1, 1, 1 ];
const yNeighbors = [ -1, 0, 1, -1, 1, -1, 0, 1 ];

const dfs = (row, col) => {
    visited[row][col] = 1;

    for (let k = 0; k < 8; k++) {
        const xNew = row + xNeighbors[k];
        const yNew = col + yNeighbors[k];

        if (
            xNew > -1 &&
            yNew > -1 &&
            xNew < ROWS &&
            yNew < COLS &&
            matrix[xNew][yNew] == 1 &&
            visited[xNew][yNew] != 1
        ) {
            dfs(xNew, yNew);
        }
    }
};

const countIslands = matrix => {
    let count = 0;

    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            if (matrix[i][j] == 1 && visited[i][j] != 1) {
                dfs(i, j);
                count++;
            }
        }
    }

    return count;
};

console.log(
    countIslands(matrix)
);

