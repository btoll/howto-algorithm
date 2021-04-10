const bfs = matrix => {
    const visited = [];
    for (let i = 0; i < matrix.length; i++) {
        visited[i] = [];

        for (let j = 0; j < matrix[0].length; j++) {
            visited[i][j] = null;
        }
    }
};

const matrix = [];
for (let i = 0; i < 10; i++) {
    matrix[i] = [];

    for (let j = 0; j < 10; j++) {
        matrix[i][j] = -1;
    }
}

console.log(bfs(matrix));

