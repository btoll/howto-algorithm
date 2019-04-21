const ticTacWin = () => {
//    const board = [];

    /*
    for (let i = 0; i < 3; i++) {
        board[i] = [];

        for (let j = 0; j < 3; j++) {
            board[i][j] = null;
        }
    }
    */

//    board[0][2] = 'X';
//    board[1][2] = 'X';
//    board[2][2] = 'X';

    const board = Array(9).fill(null);
    board[2] = 'x';
    board[5] = 'x';
    board[8] = 'x';

    console.log(board);

    const win = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    win.forEach(row => {
        const [a, b, c] = row;

        if (board[a] === 'x' && board[b] === 'x' && board[c] === 'x' )
            console.log('win!');
    });
};

console.log(ticTacWin());

