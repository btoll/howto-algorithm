//const matrix = [
//    [ 1, 1, 1],
//    [ 1, 1, 1],
//    [ 1, 1, 1]
//];

let board;
const X = 1;
const O = 2;

const check = player => {
    let won = true;

    // Check row.
    for (let y = 0; y < 3; y++) {
        won = true;

        for (let x = 0; x < 3; x++) {
            if (board[y][x] !== player) {
                won = false;
                break;
            }
        }

        if (won) break;
    }

    if (!won) {
        // Check column.
        for (let x = 0; x < 3; x++) {
            won = true;

            for (let y = 0; y < 3; y++) {
                if (board[y][x] !== player) {
                    won = false;
                    break;
                }
            }

            if (won) break;
        }
    }

    if (!won) {
        if (board[0][0] === player &&
            board[1][1] === player &&
            board[2][2] === player) {
            won = true;
        }
    }

    if (!won) {
        if (board[0][2] === player &&
            board[1][1] === player &&
            board[2][0] === player) {
            won = true;
        }
    }

    console.log(won);
};

const makeBoard = () => {
    const grid = [[], [], []];

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            grid[i][j] = -1;
        }
    }

    board = grid;
};

const move = (player, x, y) => {
    if (board[x][y] !== -1) {
        console.log('Already played!');
    } else {
        board[x][y] = player;
        check(player);
    }
};

const printBoard = () => {
    for (let i = 0; i < 3; i++) {
        console.log(...board[i]);

        /*
        for (let j = 0; j < 3; j++) {
            console.log(board[i][j]);
        }
        */
    }
};

const matrix = makeBoard();

printBoard(matrix);

move(O, 2, 0);
move(O, 1, 1);
move(O, 0, 2);

