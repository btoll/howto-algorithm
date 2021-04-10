class Graph {
    constructor() {
        this.nodes = {};
    }

    add(vertex) {
        this.nodes[vertex.name] = vertex;
    }

    find(name) {
        return this.nodes[name];
    }
}

class Node {
    constructor(name) {
        this.name = name;
        this.children = [];
    }

    add(vertext) {
        this.children.push(vertext);
    }
}

const makeGraph = () => {
    const adjacencyList = [
        [5, 6],
        [3, 4, 7],
        [],
        [],
        [2, 3, 6],
        [8],
        [9],
        [],
        [4]
    ];

    const graph = new Graph();

    for (let i = 1; i < 10; i++) {
        graph.add(new Node(i));
    }

    for (let i = 1; i < 10; i++) {
        const node = graph.find(i);

        for (let child of adjacencyList[i - 1]) {
            node.add(graph.find(child));
        }
    }

    return graph;
};

const BFS = (start, end) => {
    const graph = makeGraph();
    const startNode = graph.find(start);
    startNode.visited = true;

    const q = [];
    q.push([startNode, 0]);

    while (q.length) {
        const [node, distance] = q.pop();

        if (node.name === end) return distance;

        for (let child of node.children) {
            if (!child.visited) {
                child.visited = true;
                q.push([child, distance + 1]);
            }
        }
    }

    return -1;
};

console.log(BFS(6, 8));

