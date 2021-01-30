const isPalindrome = s => {
    for (let i = 0, j = s.length - 1; i < j; i++, j--) {
        if (s[j] !== s[i]) return false;
    }

    return true;
};

console.log(
    isPalindrome('fuluf')
);
