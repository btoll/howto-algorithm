function Trie() {
    this.root = this.node();
}

Trie.prototype = Object.create(null);

Trie.prototype.node = function () {
    return {
        children: new Map(),
        value: ''
    };
};

Trie.prototype.has = function (s) {
    let node = this.root;
    let i = 0;;

    for (; i < s.length; i++) {
        if (node.children.has(s[i])) {
            node = node.children.get(s[i]);
        } else {
            break;
        }
    }

    return (i === s.length) ?
        node.value :
        false;
};

Trie.prototype.insert = function (s) {
    let node = this.root;

    for (let i = 0; i < s.length; i++) {
        if (!node.children.has(s[i])) {
            node.children.set(s[i], this.node(s[i]));
        }

        node = node.children.get(s[i]);
    }

    node.value = s;
};

Trie.prototype.search = function (s) {
    let node = this.root;
    let j = 0;
    const found = new Set();
    const q = [];

    // Walk the length of the search string.
    for (let i = 0; i < s.length; i++) {
        if (node.children.has(s[i])) {
            node = node.children.get(s[i]);
            j++;
        }
    }

    if (j === s.length) {
        q.push(node);

        while (q.length) {
            const n = q.shift();

            if (n.value) {
                found.add(n.value);
            }

            if (n.children) {
                for (let [key, value] of n.children.entries()) {
                    q.push(value);
                }
            }
        }

        return [...found];
    } else {
        return [];
    }
};

// dog, deal, deer
// search: de

const trie = new Trie();

trie.insert('dog');
trie.insert('deal');
trie.insert('deer');
trie.insert('deacon');

//console.log(trie.has('dog'));
//console.log(trie.has('deer'));

console.log(trie.search('dea'));

