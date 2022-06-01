/* First in, first out. */
class Queue {
  /**
   * Queue constructor.
   */
  constructor() {
    this.queue = []
    this.length = 0
  }

  /**
   * Adds an element to the front of a queue.
   * @param   {number}  value
   */
  enqueue(value) {
    this.queue.push(value)
    this.length++
  }

  /**
   * Pops an element off the front of a queue.
   * @returns {number}
   */
  dequeue() {
    this.length--
    return this.queue.shift()
  }

  /**
   * Determines if a queue is empty.
   * @returns {boolean}
   */
  isEmpty() {
    return this.length == 0
  }

  /**
   * Peeks at the element at the front of the queue.
   * @returns {number}
   */
  peek() {
    return this.queue[0]
  }
}

module.exports = {
  Queue
}

const q = new Queue()
const arr = [4, 5, 2, 8, 1, 9, 6, 7, 3, 0]
for (let i of arr) q.enqueue(i)
console.log(q)
/*
Queue { queue: [ 4, 5, 2, 8, 1, 9, 6, 7, 3, 0 ], length: 10 }
*/
console.log(q.dequeue()) // 4
console.log(q)
/*
Queue { queue: [ 5, 2, 8, 1, 9, 6, 7, 3, 0 ], length: 9 } 
*/
console.log(q.peek()) // 5
