//const URLify = s =>
//    s.replace(/^\s*|\s*$/g, '').replace(/\s/g, '%20');

//const URLify = s =>
//    s.trim().split(' ').join('%20');

const URLify = (s, k) => {
    let i = 0;
    while (s[i] === ' ') i++;

    const arr = [];
    for (; i < k; i++) {
        if (s[i] === ' ') arr.push('%20');
        else arr.push(s[i]);
    }

    return arr.join('');
};

console.log(URLify('Mr John Smith       ', 13));

