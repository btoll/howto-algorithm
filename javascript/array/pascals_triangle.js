// https://leetcode.com/problems/pascals-triangle/

const pascal = rows => {
    if (rows === 0) return [];
    if (rows === 1) return [1];

    const triangle = [
        [1],
        [1, 1]
    ];

    for (let i = 1; i < rows; i++) {
        const q = [1];

        for (j = 1; j < i; j++) {
            q.push(triangle[i][j] + triangle[i][j - 1]);
        }

        q.push(1);
        triangle.push(q);
    }

    return triangle;
};

console.log(pascal(15));

