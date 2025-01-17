const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  const n = input[0];
  const arr = input.slice(1);

  const 인접리스트 = {};

  for (let i = 0; i < n; i++) {
    const [node, left, right] = arr[i].split(' ');
    인접리스트[node] = [left, right];
  }

  let preOrderResult = '';
  function preOrder(node) {
    if (node === '.' || !node) return;
    preOrderResult += node;
    preOrder(인접리스트[node][0]);
    preOrder(인접리스트[node][1]);
  }

  let inOrderResult = '';
  function inOrder(node) {
    if (node === '.' || !node) return;
    inOrder(인접리스트[node][0]);
    inOrderResult += node;
    inOrder(인접리스트[node][1]);
  }

  let postOrderResult = '';
  function postOrder(node) {
    if (node === '.' || !node) return;
    postOrder(인접리스트[node][0]);
    postOrder(인접리스트[node][1]);
    postOrderResult += node;
  }

  preOrder('A');
  inOrder('A');
  postOrder('A');

  return [preOrderResult, inOrderResult, postOrderResult].join('\n');
}

console.log(solution(input));
