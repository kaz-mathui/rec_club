class Graph {
  /**
   * Graph constructor.
   * @param   {boolean}   directed
   */
  constructor(directed = true) {
    this.nodes = {}
    this.directed = directed
  }

  /**
   * Adds a new vertex to graph, or return existing one.
   * @param   {number}    value
   * @returns {GraphNode}
   */
  addVertex(value) {
    if (this.nodes[value]) return this.nodes[value]
    else {
      const node = new GraphNode(value)
      this.nodes[value] = node
      return node
    }
  }

  /**
   * Removes vertex from graph
   * @param   {number}    value
   * @returns {GraphNode}
   */
  removeVertex(value) {
    const current = this.nodes[value]
    if (current)
      /* Removes edges connected to vertex. */
      for (const node of Object.values(this.nodes)) node.removeAdjacent(current)
    delete this.nodes[value]
    return current
  }

  /**
   * Adds an edge between two vertexes.
   * @param   {GraphNode} source
   * @param   {GraphNode} destination
   * @returns {GraphNode[]}
   */
  addEdge(source, destination) {
    const sourceNode = this.addVertex(source)
    const destinationNode = this.addVertex(destination)
    sourceNode.addAdjacent(destinationNode)
    /* Bi-directional graphs. */
    if (!this.directed) destinationNode.addAdjacent(sourceNode)
    return [sourceNode, destinationNode]
  }

  /**
   * Removes an edge between two vertexes
   * @param   {GraphNode} source
   * @param   {GraphNode} destination
   * @returns {GraphNode[]}
   */
  removeEdge(source, destination) {
    const sourceNode = this.nodes[source]
    const destinationNode = this.nodes[destination]
    if (sourceNode && destinationNode)
      sourceNode.removeAdjacent(destinationNode)
    if (!this.directed) destinationNode.removeAdjacent(sourceNode)
    return [sourceNode, destinationNode]
  }
}

class GraphNode {
  /**
   * Node constructor.
   */
  constructor(value) {
    this.value = value
    this.adjacents = []
  }

  /**
   * Adds an adjacent node.
   * @param   {GraphNode} node
   */
  addAdjacent(node) {
    this.adjacents.push(node)
  }

  /**
   * Removes an adjacent node.
   * @param   {GraphNode} node
   */
  removeAdjacent(node) {
    const index = this.adjacents.indexOf(node)
    if (index > -1) this.adjacents.splice(index, 1)
  }
}

module.exports = {
  Graph,
  GraphNode
}
