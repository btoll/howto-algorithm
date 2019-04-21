//You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
//
//    Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
//
//    For example, given the following board:
//
//[[f, f, f, f],
//    [t, t, f, t],
//    [f, f, f, f],
//    [f, f, f, f]]
//and start =
//    (3, 0)
//(bottom left) and end =
//    (0, 0)
//(top left), the minimum number of steps required to reach the end is 7, since we would need to go through
//(1, 2)
//because there is a wall everywhere else on the second row.

const matrix = [
    [false, false, false, false],
    [true, true, false, true],
    [false, false, false, false],
    [false, false, false, false]
];

const isValid = (row, col) => {
    return (
        row > -1 &&
        col > -1 &&
        row < matrix[0].length &&
        col < matrix.length
    );
};

const BFT = (matrix, start, end) => {
    if (!matrix.length) return 0;

    const visited = [];
    for (let i = 0; i < matrix.length; i++) {
        const row = [];

        for (let j = 0; j < matrix[0].length; j++) {
            row[j] = null;
        }

        visited.push(row);
    }

    // Return early if either endpoint isn't `false`.
    if (matrix[start.y][start.x] || matrix[end.y][end.x]) return -1;

    // To check bounds.
    const yCoords = [-1, 0, 0, 1];
    const xCoords = [0, -1, 1, 0];

    const q = [
        [ start, 0 ]
    ];

    while (q.length) {
        const [ cell, distance ] = q.pop();

        if (cell.y === end.y && cell.x === end.x ) return distance;

        for (let i = 0; i < 4; i++) {
            let row = cell.y + yCoords[i];
            let col = cell.x + xCoords[i];

            if (isValid(row, col) && !matrix[row][col] && !visited[row][col]) {
                visited[row][col] = true;
                q.push([{ y: row, x: col }, distance + 1]);
            }
        }
    }

    return -1;
};

const start = { y: 3, x: 0 };
const end = { y: 0, x: 0 };

console.log(BFT(matrix, start, end));

