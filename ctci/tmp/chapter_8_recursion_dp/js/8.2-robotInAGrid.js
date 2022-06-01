class Point {
  /**
   * Point constructor.
   * @param    {number} r
   * @param    {number} c
   */
  constructor(r, c) {
    this.row = r
    this.col = c
  }
}

/**
 * Gets path from top left corner of a maze to bottom right corner.
 * @param   {number[][]} maze
 * @returns {Point[]}
 */
const getPath = maze => {
  const path = []
  if (gph(maze, maze.length - 1, maze[0].length - 1, path, {})) return path
}
/**
 * Helper.
 * @param   {number[][]} maze
 * @param   {number}     row
 * @param   {number}     col
 * @param   {Point[]}    path
 * @param   {Object}     seen
 * @returns {boolean}
 */
const gph = (maze, row, col, path, seen) => {
  if (row < 0 || col < 0 || maze[row][col] === 0) return false
  const p = new Point(row, col)
  if (seen[p]) return false
  const isOrigin = row === 0 && col === 0
  if (
    isOrigin ||
    gph(maze, row - 1, col, path, seen) ||
    gph(maze, row, col - 1, path, seen)
  ) {
    path.push(p)
    return true
  }
  seen[p] = true
  return false
}

const maze = [
  [1, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 1]
]

console.log(getPath(maze))
/*
[ Point { row: 0, col: 0 },
  Point { row: 0, col: 1 },
  Point { row: 1, col: 1 },
  Point { row: 2, col: 1 },
  Point { row: 3, col: 1 },
  Point { row: 3, col: 2 },
  Point { row: 3, col: 3 } ]
*/
