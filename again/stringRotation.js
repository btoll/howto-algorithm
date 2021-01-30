const isSubstring = (s1, s2) => {
    return `${s1}${s1}`.includes(s2);
};

console.log(
    isSubstring('asdfqwer', 'eras')
);
