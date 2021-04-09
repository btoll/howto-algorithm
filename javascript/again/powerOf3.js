/*
const powerOf3 = n => {
    if (n === 1) {
        return true;
    }

    do {
        n = n / 3;
        if (n == 1) return true;
    } while (n >= 1);

    return false;
};
*/

const powerOf3 = n => {
    if (n < 1) {
        return false;
    }

    while (n % 3 == 0) {
        n /= 3;
    }

    return n === 1;
};

let i = 1;

while (i <= 10000) {
    if (powerOf3(i)) {
        console.log(i);
    }

    i++;
}

