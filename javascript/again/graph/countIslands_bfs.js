const ROWS = 10;
const COLS = 10;

const matrix = [
    [ 1, 0, 1, 0, 0, 0, 1, 1, 1, 1 ],
    [ 0, 0, 1, 0, 1, 0, 1, 0, 0, 0 ],
    [ 1, 1, 1, 1, 0, 0, 1, 0, 0, 0 ],
    [ 1, 0, 0, 1, 0, 1, 0, 0, 0, 0 ],
    [ 1, 1, 1, 1, 0, 0, 0, 1, 1, 1 ],
    [ 0, 1, 0, 1, 0, 0, 1, 1, 1, 1 ],
    [ 0, 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
    [ 0, 0, 0, 1, 0, 0, 1, 1, 1, 0 ],
    [ 1, 0, 1, 0, 1, 0, 0, 1, 0, 0 ],
    [ 1, 1, 1, 1, 0, 0, 0, 1, 1, 1 ]
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

const bfs = (row, col) => {
    visited[row][col] = 1;

    const queue = [
        [ row, col ]
    ];

    while (queue.length) {
        const pair = queue.pop();

        for (let k = 0; k < 8; k++) {
            const xNew = pair[0] + xNeighbors[k];
            const yNew = pair[1] + yNeighbors[k];

            if (
                xNew > -1 &&
                yNew > -1 &&
                xNew < ROWS &&
                yNew < COLS &&
                matrix[xNew][yNew] == 1 &&
                visited[xNew][yNew] != 1
            ) {
                visited[xNew][yNew] = 1
                queue.unshift([xNew, yNew]);
            }
        }
    }
};

const countIslands = matrix => {
    let count = 0;

    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            if (matrix[i][j] == 1 && visited[i][j] != 1) {
                bfs(i, j);
                count++;
            }
        }
    }

    return count;
};

console.log(
    countIslands(matrix)
);

