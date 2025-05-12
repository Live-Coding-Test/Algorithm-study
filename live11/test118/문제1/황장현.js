class MinHeap {
  constructor() {
    this.heap = [];
  }
  push(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return min;
  }

  bubbleUp() {
    let index = this.heap.length - 1;

    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex] <= this.heap[index]) break;
      [this.heap[parentIndex], this.heap[index]] = [
        this.heap[index],
        this.heap[parentIndex],
      ];
      index = parentIndex;
    }
  }

  bubbleDown() {
    let index = 0;
    const length = this.heap.length;

    while (true) {
      const left = 2 * index + 1;
      const right = 2 * index + 2;
      let smallest = index;

      if (left < length && this.heap[left] < this.heap[smallest]) {
        smallest = left;
      }

      if (right < length && this.heap[right] < this.heap[smallest]) {
        smallest = right;
      }

      if (smallest === index) break;

      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];

      index = smallest;
    }
  }

  least() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }
}

const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const T = input[0];
  let result = [];
  let lineIndex = 1;

  for (let t = 0; t < T; t++) {
    const K = parseInt(input[lineIndex++]);
    const files = input[lineIndex++].split(' ').map(Number);
    const minHeap = new MinHeap();
    for (let i = 0; i < K; i++) {
      minHeap.push(files[i]);
    }

    let sum = 0;
    while (minHeap.size() > 1) {
      const a = minHeap.pop();
      const b = minHeap.pop();
      sum += a + b;
      minHeap.push(a + b);
    }

    result.push(sum);
  }

  return result.join('\n');
}

console.log(solution(input));
