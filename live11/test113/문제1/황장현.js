const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

function isConsistent(phoneNumbers) {
  const root = new TrieNode();

  for (const number of phoneNumbers) {
    let node = root;

    for (let i = 0; i < number.length; i++) {
      const char = number[i];

      if (!node.children[char]) {
        node.children[char] = new TrieNode();
      }

      node = node.children[char];

      if (node.isEnd) {
        return false;
      }
    }
    if (Object.keys(node.children).length > 0) {
      return false;
    }
    node.isEnd = true;
  }

  return true;
}

function solution(input) {
  const t = parseInt(input[0]);
  let index = 1;

  for (let i = 0; i < t; i++) {
    const n = parseInt(input[index]);
    const phoneNumbers = input.slice(index + 1, index + 1 + n);
    isConsistent(phoneNumbers) ? console.log('YES') : console.log('NO');

    index += n + 1;
  }
}

solution(input);
