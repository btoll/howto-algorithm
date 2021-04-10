const maxProfit = prices => {
    let low = prices[0];
    let max = -1;

    for (let i = 1; i < prices.length; i++) {
        if (low > prices[i]) {
            low = prices[i];
        } else if (prices[i] - low > max) {
            max = prices[i] - low;
        }
    }

    return max;
};

console.log(
    maxProfit([ 14, 11, 15, 7, 10, 6 ]),
    maxProfit([ 14, 11, 10, 8, 9, 6 ]),
    maxProfit([ 3, 2, 6, 5, 0, 3 ]),
    maxProfit([ 7, 1, 5, 3, 6, 4 ])
);

