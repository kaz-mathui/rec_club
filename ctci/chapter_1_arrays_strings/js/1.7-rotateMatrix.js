/* O(n**2) solution, best case scenario  */

/**
 * Rotates a NxN matrix 90 degrees in place.
 * @param   {number[][]} matrix
 * @returns {boolean}
 */
const rotateMatrixBy90 = matrix => {
  if (!matrix.length || matrix.length != matrix[0].length) return false
  const n = matrix.length
  for (let layer = 0; layer < Math.floor(n / 2); layer++) {
    const first = layer
    const last = n - 1 - layer
    let offset = 0
    for (let i = first; i < last; i++) {
      /* save top */
      const top = matrix[first][i]
      /* left -> top */
      matrix[first][i] = matrix[last - offset][first]
      /* bottom -> left */
      matrix[last - offset][first] = matrix[last][last - offset]
      /* right -> bottom */
      matrix[last][last - offset] = matrix[i][last]
      /* bottom > top */
      matrix[i][last] = top
      offset++
    }
  }
  return true
}

/**
 * Prints matrix row by row.
 * @param   {number[][]} matrix
 */
const printMatrix = matrix => {
  for (let width of matrix) {
    console.log(width)
  }
  console.log("------------------")
}

const matrix1 = [
  [0, 1],
  [2, 3]
]
const matrix2 = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8]
]
const matrix3 = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10, 11],
  [12, 13, 14, 15]
]
const matrix4 = [
  [0, 1, 2, 3, 4],
  [5, 6, 7, 8, 9],
  [10, 11, 12, 13, 14],
  [15, 16, 17, 18, 19],
  [20, 21, 22, 23, 24]
]

printMatrix(matrix1)
rotateMatrixBy90(matrix1)
printMatrix(matrix1)

printMatrix(matrix2)
rotateMatrixBy90(matrix2)
printMatrix(matrix2)

printMatrix(matrix3)
rotateMatrixBy90(matrix3)
printMatrix(matrix3)

printMatrix(matrix4)
rotateMatrixBy90(matrix4)
printMatrix(matrix4)
