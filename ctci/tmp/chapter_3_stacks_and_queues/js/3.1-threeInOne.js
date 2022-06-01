class FixedMultiStack {
  /**
   * Fixed multi-stack constructor.
   * @param   {number}  stackSize
   */
  constructor(stackSize) {
    this.numberOfStacks = 3
    this.stackCapacity = stackSize
    this.values = Array(stackSize * 3).fill(0)
    /* Array of sizes of sub-arrays. */
    this.sizes = Array(3).fill(0)
  }

  /**
   * Pushes an element into a given stack.
   * @param   {number}  stackNum
   * @param   {number}  value
   */
  push(stackNum, value) {
    if (this.isFull(stackNum)) {
      throw new Error("stack is full")
    }
    this.sizes[stackNum]++
    const index = this.indexOfTop(stackNum)
    this.values[index] = value
  }

  /**
   * Pops the top element off a fixed multi-stack.
   * @param   {number}  stackNum
   * @returns {number}
   */
  pop(stackNum) {
    if (this.isEmpty(stackNum)) {
      throw new Error("stack is empty")
    }
    const index = this.indexOfTop(stackNum)
    const value = this.values[index]
    this.values[index] = 0
    this.sizes[stackNum]--
    return value
  }

  /**
   * Determines if a fixed multi-stack is empty or not.
   * @param   {number}  stackNum
   * @returns {boolean}
   */
  isEmpty(stackNum) {
    return this.sizes[stackNum] == 0
  }

  /**
   * Determines if a fixed multi-stack is full or not.
   * @param   {number}  stackNum
   * @returns {boolean}
   */
  isFull(stackNum) {
    return this.sizes[stackNum] == this.stackCapacity
  }

  /**
   * Returns the top index of a given stack.
   * @param   {number}  stackNum
   * @returns {number}
   */
  indexOfTop(stackNum) {
    const offset = stackNum * this.stackCapacity
    const size = this.sizes[stackNum]
    return offset + size - 1
  }
}

const fms = new FixedMultiStack(5)
console.log(fms)
/* 
FixedMultiStack {
  numberOfStacks: 3,
  stackCapacity: 5,
  values: [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  sizes: [ 0, 0, 0 ] }
*/
console.log(fms.indexOfTop(0)) // -1
console.log(fms.indexOfTop(1)) // 4
console.log(fms.indexOfTop(2)) // 9
fms.push(0, 16)
fms.push(0, 8)
fms.push(0, 4)
fms.push(0, 2)
fms.push(0, 1)
/* fms.push(0, -1) // error */
fms.push(1, 99)
fms.pop(1)
/* fms.pop(1) // error */
console.log(fms)
/*
FixedMultiStack {
  numberOfStacks: 3,
  stackCapacity: 5,
  values: [ 16, 8, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  sizes: [ 5, 0, 0 ] }
*/
