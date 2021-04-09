const m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
//
//    'IV': 4,
//    'IX': 9,
//    'XL': 40,
//    'XC': 90,
//    'CD': 400,
//    'CM': 900
};

/*
const romanToInt = s => {
    s = s.toUpperCase();

    let count = 0;

    for (let i = 0, j = 1; i < s.length; i++, j++) {
        const curr = s[i];
        const lookahead = `${curr}${s[j]}`;

        if (m[lookahead]) {
            count += m[lookahead];
            i++;
            j++;
        } else {
            count += m[curr];
        }
    }

    return count;
};
*/

// This one is best.
const romanToInt = s => {
    s = s.toUpperCase();

    let count = 0;

    for (let i = 0; i < s.length; i++) {
        const curr = m[s[i]];
        // In JavaScript, don't worry about the bounds check :)
        const next = m[s[i + 1]];

        if (next > curr) {
            count += next - curr;
            i++;
        } else {
            count += curr;
        }
    }

    return count;
};

//     III => 3
//      XL => 40
//   MCMIV => 1904
// MCMXCIV => 1994

console.log(
    romanToInt('III'),
    romanToInt('XL'),
    romanToInt('MCMIV'),
    romanToInt('MCMXCIV')
);

