const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
const N = parseInt(input[0]);
const M = parseInt(input[1]);

const result = [];
const visited = Array(N + 1).fill(false);

function backtracking(path) {
  if (path.length === M) {
    console.log(path.join(' '));
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
      visited[i] = true;
      path.push(i);
      backtracking(path);
      path.pop();
      visited[i] = false;
    }
  }
}

backtracking([]);
