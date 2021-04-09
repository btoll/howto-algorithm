const conversion = (n1, n2) => {
    let k = 0;
    let max = Math.max(n1, n2);

    do {
        if ((n1 & 1) !== (n2 & 1)) k++;
        n1 >>= 1;
        n2 >>= 1;
    } while (max >>= 1 > -1);

    return k;
};

console.log(conversion(179, 205));
//console.log(conversion(29, 15));

