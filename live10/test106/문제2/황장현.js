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
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function solution(input) {
  const [N, M] = input[0];
  const adjList = Array.from({ length: N + 1 }, () => []);

  for (let i = 1; i <= M; i++) {
    const [A, B, C] = input[i];
    adjList[A].push([B, C]);
    adjList[B].push([A, C]);
  }

  function dijkstra(start) {
    const distances = Array(N + 1).fill(Infinity);
    const minHeap = new MinHeap();
    minHeap.push([0, start]);
    distances[start] = 0;

    while (minHeap.size() > 0) {
      const [currentCost, currentNode] = minHeap.pop();

      if (currentCost > distances[currentNode]) continue;

      for (const [nextNode, nextCost] of adjList[currentNode]) {
        const newCost = currentCost + nextCost;

        if (newCost < distances[nextNode]) {
          distances[nextNode] = newCost;
          minHeap.push([newCost, nextNode]);
        }
      }
    }

    return distances[N];
  }

  return dijkstra(1);
}

console.log(solution(input));
