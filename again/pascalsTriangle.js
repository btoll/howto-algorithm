const pascalsTriangle = numRows => {
    if (!numRows) {
        return [];
    }

    if (numRows === 1) {
        return [[1]];
    }

    if (numRows === 2) {
        return [[1], [1, 1]];
    }

    const triangle = [[1], [1, 1]];

    for (let i = 2; i < numRows; i++) {
        let j = 0;
        const iter = i - 1;
        const a = [1];

        while (j < iter) {
            a.push(triangle[i - 1][j] + triangle[i - 1][j + 1]);
            j++;
        }

        a.push(1);

        triangle.push(a);
    }

    return triangle;
};

console.log(
    pascalsTriangle(10)
);

