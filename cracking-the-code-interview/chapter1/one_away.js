const insertChar = (s1, s2) => {
    let i1 = 0;
    let i2 = 0;

    while (i1 < s1.length && i2 < s2.length) {
        if (s1[i1] !== s2[i2]) {
            if (i1 !== i2) return false;
            i2++;
        } else {
            i1++;
            i2++;
        }
    }

    return true;
};

const replaceChar = (first, second) => {
    let oneAway = false;

    for (let i = 0; i < first.length; i++) {
        if (first[i] !== second[i]) {
            if (oneAway) return false;
            oneAway = true;
        }
    }

    return oneAway;
};

const oneEditAway = (first, second) => {
    const l1 = first.length;
    const l2 = second.length;

    if (l1 === l2) return replaceChar(first, second);
    else if (l1 + 1 === l2) return insertChar(first, second);
    else if (l1 - 1 === l2) return insertChar(second, first);
    else return false;
};

const first = 'pale';
const second = 'ple';

console.log(oneEditAway(first, second));

