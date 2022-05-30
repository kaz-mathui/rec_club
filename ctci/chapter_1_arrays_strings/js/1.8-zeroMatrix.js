/* O(n**2) solution, best case */

/**
 * Prints matrix row by row.
 * @param   {number[][]} matrix
 */
const printMatrix = matrix => {
  for (const width of matrix) {
    console.log(width)
  }
  console.log("------------------")
}

/**
 * Sets zeros for all values in same row and column as existing zeroes.
 * @param   {number[][]} matrix
 */
const setZeros = matrix => {
  /* Store all rows and columns where there is a zero in arrays. */
  const rows = []
  const columns = []
  for (let i = 0; i < matrix.length; i++)
    for (let j = 0; j < matrix[0].length; j++)
      if (matrix[i][j] === 0) {
        columns.push(j)
        rows.push(i)
      }
  /* rows */
  for (const r of rows) nullifyRow(matrix, r)
  /* columns */
  for (const c of columns) nullifyColumn(matrix, c)
}

/**
 * Set zeros for all values in a given row of a matrix.
 * @param   {number[][]} matrix
 * @param   {number}   row
 */
const nullifyRow = (matrix, row) => {
  for (let i = 0; i < matrix[0].length; i++) matrix[row][i] = 0
}

/**
 * Set zeros for all values in a given column of a matrix.
 * @param   {number[][]} matrix
 * @param   {number}   column
 */
const nullifyColumn = (matrix, column) => {
  for (let i = 0; i < matrix.length; i++) matrix[i][column] = 0
}

const matrix1 = [
  [2, 2, 2, 2, 2],
  [2, 2, 0, 2, 2],
  [2, 2, 2, 2, 2],
  [2, 2, 2, 2, 2]
]

printMatrix(matrix1)
setZeros(matrix1)
printMatrix(matrix1)
