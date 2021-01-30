// https://leetcode.com/articles/fibonacci-number/
// https://www.youtube.com/watch?v=sj8Sg8qnjOg
// https://www.youtube.com/watch?v=c8ccsE_IumM
const getGoldenRatio = n => {
    // Binet's formula:
    //
    //      ( 1 + math.Sqrt(5) ) / 2
    //
    const goldenRatio = (1 + 5 ** 0.5) / 2; // 1.618033988749895
    return (goldenRatio ** n + 1) / 5 ** 0.5 >> 0;
};

const fib = n => {
    let j = 0;

    while (j <=n) {
        console.log(getGoldenRatio(j));
        j++;
    }
};

fib(20);

