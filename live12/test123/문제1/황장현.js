const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const G = input[0];
const P = input[1];
const planes = input.slice(2);

const parent = Array.from({ length: G + 1 }, (_, i) => i);

function find(x) {
  if (parent[x] === x) return x;
  return (parent[x] = find(parent[x]));
}

function union(x, y) {
  const rootX = find(x);
  const rootY = find(y);
  if (rootX !== rootY) {
    parent[rootX] = rootY;
  }
}

let answer = 0;

for (let i = 0; i < P; i++) {
  const gate = planes[i];
  const availableGate = find(gate);

  if (availableGate === 0) break;

  union(availableGate, availableGate - 1);

  answer++;
}

console.log(answer);
