const ROWS = 10;
const COLS = 10;

const makeMatrix = () => ([
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]);

const xNeighbors = [ -1, -1, -1, 0, 0, 1, 1, 1 ];
const yNeighbors = [ -1, 0, 1, -1, 1, -1, 0, 1 ];

const generate = () => {
    const matrix = makeMatrix();
    const next = makeMatrix();

    // Don't test boundaries!
    for (let i = 1; i < ROWS - 1; i++) {
        for (let j = 1; j < COLS - 1; j++) {
            let numAlive = 0;

            /*
            for (let k = -1; k <= 1; k++) {
                for (let l = -1; l <= 1; l++) {
                    numAlive += matrix[i + k][j + l];
                }
            }

            numAlive -= matrix[i][j];
            */

            for (let k = 0; k < 8; k++) {
                const newX = xNeighbors[k];
                const newY = yNeighbors[k];

                numAlive += matrix[i + newX][j + newY];
            }

            let cell = matrix[i][j];

            if (cell && numAlive < 2) {
                next[i][j] = 0;
            } else if (cell && numAlive > 3) {
                next[i][j] = 0;
            } else if (cell == 0 && numAlive == 3) {
                next[i][j] = 1;
            } else {
                next[i][j] = matrix[i][j];
            }
        }
    }

    return next;
};

const print = matrix => {
    for (let i = 0; i < ROWS; i++) {
        for (let j = 0; j < COLS; j++) {
            if (matrix[i][j]) {
                matrix[i][j] = '*';
            } else {
                matrix[i][j] = '.';
            }
        }
    }

    console.log(matrix);
};

const gameOfLife = () => {
    console.log('before');
    print(makeMatrix());
    console.log();
    console.log('after');
    print(generate());
};

gameOfLife();

