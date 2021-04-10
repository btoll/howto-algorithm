const parens = str => {
    const s = [];

    for (let char of str) {
        if (char === '(') s.push(char);
        if (char === ')') {
            if (s.length === 0) {
                s.push(char);
                break;
            }

            s.pop();
        }
    }

    return s;
};

const str = 'He(ll(o) W)o()r(ld)';

console.log(parens(str));

