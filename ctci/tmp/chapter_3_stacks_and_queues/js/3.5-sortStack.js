const { Stack } = require("./stack")

class Stack_3_5 extends Stack {
  /**
   * Sorts a stack using a secondary stack as a buffer.
   * O(n**2) time complexity and O(n) space complexity.
   */
  sort() {
    const buffer = new Stack()
    while (!this.isEmpty()) {
      const tmp = this.pop()
      while (!buffer.isEmpty() && buffer.peek() < tmp) {
        /* If peeked value in buffer is less than temp, place back in stack. */
        this.push(buffer.pop())
      }
      buffer.push(tmp)
    }
    /* Place everything in buffer back into stack. */
    while (!buffer.isEmpty()) this.push(buffer.pop())
  }
}

const s = new Stack_3_5()
const arr = [4, 5, 2, 8, 1, 9, 6, 7, 3, 0]
for (let i of arr) s.push(i)
console.log(s) // Stack_3_5 { stack: [ 4, 5, 2, 8, 1, 9, 6, 7, 3, 0 ], length: 10 }
s.sort()
console.log(s) // Stack_3_5 { stack: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ], length: 10 }
