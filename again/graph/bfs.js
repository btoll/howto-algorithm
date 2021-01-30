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

Graph.prototype.bfs = function (start = 0) {
    const vertices = this.graph;
    const queue = [start];
    const visited = new Array(vertices).fill(false);

    while (queue.length) {
        let s = queue.pop();
        let list = this.graph[s];
        let a = [];

        if (!visited[s]) {
            visited[s] = true;

            while (list) {
                a.push(list.vertex);
                list = list.next;
            }

            console.log(
                `Adjaceny list of vertex ${s} => `,
                a.reverse().join(', ')
            );

            queue.unshift((s + 1) % vertices.length);
        }
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

graph.bfs(4);

