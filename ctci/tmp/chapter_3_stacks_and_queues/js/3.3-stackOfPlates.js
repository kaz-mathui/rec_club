const { Stack } = require("./stack")

class StackWithCapacity extends Stack {
  /**
   * Stack with capacity constructor.
   * @param   {number}  [capacity=5]
   */
  constructor(capacity = 5) {
    super()
    this.capacity = capacity
  }

  /**
   * Pushes an element to the top of the stack.
   * @param   {number}  value
   */
  push(value) {
    if (this.isFull()) throw new Error("stack is full")
    this.stack.push(value)
    this.length++
  }

  /**
   * Determines if a stack with capacity is full.
   * @returns {boolean}
   */
  isFull() {
    return this.length === this.capacity
  }
}

swc = new StackWithCapacity(5)
swc.push(1)
swc.push(1)
swc.push(1)
swc.push(1)
swc.push(1)
/* swc.push(1) error */
console.log(swc)
/*
StackWithCapacity { stack: [ 1, 1, 1, 1, 1 ], length: 5, capacity: 5 }
*/

class SetOfStacks {
  /**
   * Set of stacks constructor.
   */
  constructor() {
    this.stacks = []
    this.stacksLength = 0
  }

  /**
   * Pushes an element to the top of the stack.
   * @param   {number}  value
   */
  push(value) {
    const last = this.getLastStack()
    if (last != null && !last.isFull()) {
      /* Add to last stack. */
      last.push(value)
    } else {
      /* Create new stack. */
      const newStack = new StackWithCapacity()
      newStack.push(value)
      this.stacks.push(newStack)
      this.stacksLength++
    }
  }

  /**
   * Pops an element off the top of the stack.
   * @returns  {number}
   */
  pop() {
    const last = this.getLastStack()
    if (last === null) throw new Error("empty stack of stacks")
    const value = last.pop()
    /* If stack is empty, remove it from stacks. */
    if (last.isEmpty()) {
      this.stacks.pop()
      this.stacksLength--
    }
    return value
  }

  /**
   * Returns the last stack in set of stacks.
   * @returns {StackWithCapacity}
   */
  getLastStack() {
    if (this.stacksLength === 0) return null
    return this.stacks[this.stacksLength - 1]
  }
}

const sos = new SetOfStacks(3)
console.log(sos)
/*
SetOfStacks { stacks: [], stacksLength: 0 }
*/
const arr = [1, 2, 3, 4, 5, 6, 7]
for (let i of arr) sos.push(i)
console.log(sos)
/*
SetOfStacks {
  stacks:
   [ StackWithCapacity { stack: [Array], length: 5, capacity: 5 },
     StackWithCapacity { stack: [Array], length: 2, capacity: 5 } ],
  stacksLength: 2 }
*/
/* remove 4 items */
for (let i of Array(4)) sos.pop()
console.log(sos)
/*
SetOfStacks {
  stacks:
   [ StackWithCapacity { stack: [Array], length: 3, capacity: 5 } ],
  stacksLength: 1 }
*/
