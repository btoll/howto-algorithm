/*
 * https://www.geeksforgeeks.org/graph-and-its-representations/
 *
 *  0 ----- 1
 *  |   ___/|\
 *  |  /    | 2
 *  | /     |/
 *  4 ----- 3
 *
*/

function Graph(vertices) {
    this.vertices = vertices;
    this.graph = new Array(vertices).fill(null);
}

Graph.prototype.addEdge = function (src, dst) {
    let node = new AdjacencyList(dst);
    node.next = this.graph[src];
    this.graph[src] = node;

    // Since the graph is undirected, the edges must be symmetric!
    node = new AdjacencyList(src);
    node.next = this.graph[dst];
    this.graph[dst] = node;
};

// Print the matrix.
Graph.prototype.print = function () {
    for (let i = 0; i < this.vertices; i++) {
        let node = this.graph[i];
        const vertices = [];

        while (node) {
            vertices.push(node.vertex);
            node = node.next;
        }

        console.log(
            `Adjaceny list of vertex ${i} => `,
            vertices.reverse().join(', ')
        );
    }
};

function AdjacencyList(n) {
    this.vertex = n;
    this.next = null;
}

const graph = new Graph(5);

// source, destination
graph.addEdge(0, 1);
graph.addEdge(0, 4);
graph.addEdge(1, 2);
graph.addEdge(1, 3);
graph.addEdge(1, 4);
graph.addEdge(2, 3);
graph.addEdge(3, 4);
//console.log('graph.nodes', graph.nodes);

graph.print();

