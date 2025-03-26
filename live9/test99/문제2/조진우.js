const fs = require("fs");
const input = fs
  .readFileSync("./input.txt", "utf8")
  // .readFileSync("/dev/stdin", "utf8")
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.trim().split(" ").map(Number));

function solution(input) {
  const [N, M] = input[0];
  const arr = input[1];
  arr.sort((a, b) => a - b); // 사전 순 출력을 위해 정렬

  const visited = Array(N).fill(false);
  const path = [];

  function dfs(depth) {
    if (depth === M) {
      console.log(path.join(" ")); // 바로 출력!
      return;
    }

    for (let i = 0; i < N; i++) {
      if (visited[i]) continue;

      visited[i] = true;
      path.push(arr[i]);
      dfs(depth + 1);
      path.pop();
      visited[i] = false;
    }
  }

  dfs(0); // 시작
}

solution(input);
