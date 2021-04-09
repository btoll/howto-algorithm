/*
const stringRotation = (s1, s2) => {
    for (let i = 0; i < s2.length; i++) {
        const rotation = s2.substr(i) + s2.substr(0, i);
        if (s1 === rotation) return true;
    }

    return false;
};
*/

// 0(a+b)
const isSubstring = (s1, s2) =>
//    (s2 + s2).includes(s1);
    !!~(s2 + s2).indexOf(s1);

// O(n)
const stringRotation = (s1, s2) => {
    if (s1.length !== s2.length) return false;
    return isSubstring(s1, s2);
};

const s1 = 'waterbottle';
const s2 = 'erbottlewat';

console.log(stringRotation(s1, s2));

