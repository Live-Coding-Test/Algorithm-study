class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(node) {
    this.heap.push(node);
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
    let i = this.heap.length - 1;
    while (i > 0) {
      const parent = Math.floor((i - 1) / 2);
      if (this.heap[parent][0] <= this.heap[i][0]) break;
      [this.heap[parent], this.heap[i]] = [this.heap[i], this.heap[parent]];
      i = parent;
    }
  }

  bubbleDown() {
    let i = 0;
    const len = this.heap.length;
    while (true) {
      const left = 2 * i + 1;
      const right = 2 * i + 2;
      let smallest = i;

      if (left < len && this.heap[left][0] < this.heap[smallest][0])
        smallest = left;
      if (right < len && this.heap[right][0] < this.heap[smallest][0])
        smallest = right;
      if (smallest === i) break;

      [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
      i = smallest;
    }
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
  const [V, E] = input[0];
  const K = input[1][0];
  const edges = input.slice(2);

  const graph = Array.from({ length: V + 1 }, () => []);
  for (const [u, v, w] of edges) {
    graph[u].push([v, w]);
  }

  const ans = Array(V + 1).fill(Infinity);
  ans[K] = 0;

  const minHeap = new MinHeap();
  minHeap.push([0, K]);

  while (minHeap.size()) {
    const [dis, node] = minHeap.pop();
    if (dis > ans[node]) continue;

    for (const [v, w] of graph[node]) {
      if (ans[v] > dis + w) {
        ans[v] = dis + w;
        minHeap.push([ans[v], v]);
      }
    }
  }

  return ans
    .slice(1)
    .map((x) => (x === Infinity ? 'INF' : x))
    .join('\n');
}

console.log(solution(input));
