/* First in, last out. */
class Stack {
  constructor() {
    /**
     * Stack constructor.
     */
    this.stack = []
    this.length = 0
  }

  /**
   * Pushes an element to the top of the stack.
   * @param   {number}  value
   */
  push(value) {
    this.stack.push(value)
    this.length++
  }

  /**
   * Pops an element off the top of the stack.
   * @returns {number}
   */
  pop() {
    this.length--
    return this.stack.pop()
  }

  /**
   * Determines if a stack is empty.
   * @returns {boolean}
   */
  isEmpty() {
    return this.length === 0
  }

  /**
   * Peeks at the element at the top of the stack.
   * @returns {number}
   */
  peek() {
    return this.stack[this.length - 1]
  }
}

module.exports = {
  Stack
}

const st = new Stack()
console.log(st) // Stack { stack: [], length: 0 }
st.push(1)
st.push(2)
st.push(4)
console.log(st.peek()) // 4
st.pop()
console.log(st) // Stack { stack: [ 1, 2 ], length: 2 }
