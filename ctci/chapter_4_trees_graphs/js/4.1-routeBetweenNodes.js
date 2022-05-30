const { Graph } = require('./graph')

/**
 * Searches a graph to see if there is a route between two nodes.
 * @param   {Graph}   graph
 * @param   {number}  start
 * @param   {number}  end
 * @returns {boolean}
 */
const search = (graph, start, end) => {
  if (start === end) return true
  const queue = [start]
  const visited = {}
  visited[start.value] = true
  while (queue.length) {
    let curr = queue.shift()
    if (curr) {
      for (let neighbor of curr.adjacents) {
        if (!visited[neighbor.value]) {
          if (neighbor === end) {
            return true
          } else queue.push(neighbor)
        }
        visited[neighbor.value] = true
      }
    }
  }
  return false
}

const g = new Graph()
const sf = g.addVertex('sf')
const hayward = g.addVertex('hayward')
const sj = g.addVertex('sj')
g.addEdge('oakland', 'sf')
g.addEdge('oakland', 'berkeley')
g.addEdge('sf', 'san bruno')
g.addEdge('oakland', 'san leandro')
g.addEdge('san leandro', 'hayward')
g.addEdge('san bruno', 'hayward')
console.log(g)
/*
Graph {
  nodes:
   { sf: Node { value: 'sf', adjacents: [Array] },
     hayward: Node { value: 'hayward', adjacents: [Array] },
     sj: Node { value: 'sj', adjacents: [] },
     oakland: Node { value: 'oakland', adjacents: [Array] },
     berkeley: Node { value: 'berkeley', adjacents: [Array] },
     'san bruno': Node { value: 'san bruno', adjacents: [Array] },
     'san leandro': Node { value: 'san leandro', adjacents: [Array] } } }
*/
console.log(search(g, sf, hayward)) // true
console.log(search(g, sf, sj)) // false
g.addEdge('sj', 'hayward')
console.log(search(g, sf, sj)) // true
g.removeVertex('sj')
console.log(search(g, sf, sj)) // false
