const { Stack } = require("./stack")

class StackWithMin extends Stack {
  /**
   * Stack with minimum constructor.
   */
  constructor() {
    super()
    /* New stack with minimums. */
    this.s2 = new Stack()
  }

  /**
   * Pushes an element to the top of the stack.
   * @param   {number}  value
   */
  push(value) {
    if (value < this.min()) this.s2.push(value)
    super.push(value)
  }

  /**
   * Pops an element off the top of the stack.
   * @returns {number}
   */
  pop() {
    const value = super.pop()
    /* If min is getting popped, remove from second list also. */
    if (value == this.min()) this.s2.pop()
    return value
  }

  /**
   * Return the minimum value of the stack.
   * @returns {number}
   */
  min() {
    return this.s2.isEmpty() ? Number.MAX_SAFE_INTEGER : this.s2.peek()
  }
}

swm = new StackWithMin()
console.log(swm)
/*
StackWithMin {
  stack: [],
  length: 0,
  s2: Stack { stack: [], length: 0 } }
*/

console.log(swm.min()) // 9007199254740991
swm.push(5)
swm.push(10)
swm.push(-15)
swm.push(20)
console.log(swm)
/* 
StackWithMin {
  stack: [ 5, 10, -15, 20 ],
  length: 4,
  s2: Stack { stack: [ 5, -15 ], length: 2 } }
*/
console.log(swm.min()) // -15
console.log(swm.pop()) // 20
console.log(swm.pop()) // -15
console.log(swm)
/* 
StackWithMin {
  stack: [ 5, 10 ],
  length: 2,
  s2: Stack { stack: [ 5 ], length: 1 } }
*/
