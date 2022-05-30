const { Graph } = require('./graph')

/* TOPOLOGICAL SORT */

class Project {
  /**
   * Project constructor.
   * @param   {string}  name
   */
  constructor(name) {
    this.name = name
    this.children = []
    this.map = new Set()
    this.dependencies = 0
  }

  /**
   * Adds an adjacent node.
   * @param   {Project} node
   */
  addAdjacent(node) {
    if (!this.map.has(node.name)) {
      this.children.push(node)
      this.map.add(node.name)
      node.incrementDependencies()
    }
  }

  /**
   * Increases dependencies by 1.
   */
  incrementDependencies() {
    this.dependencies++
  }

  /**
   * Decreases dependencies by 1.
   */
  decrementDependencies() {
    this.dependencies--
  }
}

class Graph4_1 extends Graph {
  /**
   * Graph constructor.
   */
  constructor() {
    super()
    this.nodesArray = []
  }

  /**
   * Adds a new vertex to graph, or return existing one.
   * @param   {number}  value
   * @returns {Project}
   */
  addVertex(value) {
    if (this.nodes[value]) {
      return this.nodes[value]
    } else {
      const node = new Project(value)
      this.nodes[value] = node
      this.nodesArray.push(node)
      return node
    }
  }
}

/**
 * Finds a correct build order.
 * @param   {string[][]}  dependencies
 * @returns {Project[]}
 */
const findBuildOrder = dependencies => {
  const graph = buildGraph(dependencies)
  return orderProjects(graph.nodesArray)
}

/**
 * Builds the graph, adding the edge (a, b) if b is dependent on a. Assumes
 * a pair is listed in "build order". The pair (a, b) in dependencies
 * indicates that b depends on a and a must be built before b.
 * @param   {string[][]}  dependencies
 * @returns {Graph4_1}
 */
const buildGraph = dependencies => {
  const graph = new Graph4_1()
  for (let dependency of dependencies) {
    const first = dependency[0]
    const second = dependency[1]
    graph.addEdge(first, second)
  }
  return graph
}

/**
 * Returns a list of the projects in a correct build order.
 * @param   {Project[]} projects
 * @returns {Project[]}
 */
const orderProjects = projects => {
  const order = []
  /* Add roots to the build order first. */
  let endOfList = addNonDependent(order, projects, 0)
  let toBeProcessed = 0
  while (toBeProcessed < order.length) {
    let current = order[toBeProcessed]
    /* We have a circular dependency since there are no remaining
     * projects with zero dependencies. */
    if (!current) return
    let children = current.children
    for (let child of children) child.decrementDependencies()
    endOfList = addNonDependent(order, children, endOfList)
    toBeProcessed++
  }

  return order
}

/**
 * A helper function to insert projects with zero dependencies into the
 * order array, starting at index offset.
 * @param   {Project[]} order
 * @param   {Project[]} projects
 * @param   {number}    offset
 * @returns {number}
 */
const addNonDependent = (order, projects, offset) => {
  for (let project of projects) {
    if (project.dependencies === 0) {
      order[offset] = project
      offset++
    }
  }
  return offset
}

const dependencies = [
  ['a', 'e'],
  ['b', 'a'],
  ['c', 'a'],
  ['f', 'a'],
  ['f', 'b'],
  ['f', 'c'],
  ['d', 'g'],
  ['b', 'e']
]

let buildOrder = findBuildOrder(dependencies)
console.log(buildOrder)
/* 
[ Project {
    name: 'f',
    children: [ [Project], [Project], [Project] ],
    map: Set { 'a', 'b', 'c' },
    dependencies: 0 },
  Project {
    name: 'd',
    children: [ [Project] ],
    map: Set { 'g' },
    dependencies: 0 },
  Project {
    name: 'b',
    children: [ [Project], [Project] ],
    map: Set { 'a', 'e' },
    dependencies: 0 },
  Project {
    name: 'c',
    children: [ [Project] ],
    map: Set { 'a' },
    dependencies: 0 },
  Project { name: 'g', children: [], map: Set {}, dependencies: 0 },
  Project {
    name: 'a',
    children: [ [Project] ],
    map: Set { 'e' },
    dependencies: 0 },
  Project { name: 'e', children: [], map: Set {}, dependencies: 0 } ]
*/
console.log(buildOrder.map(project => project.name))
/* [ 'f', 'd', 'b', 'c', 'g', 'a', 'e' ] */
