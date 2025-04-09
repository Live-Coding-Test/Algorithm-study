function solution(begin, target, words) {
  if (!words.includes(target)) return 0;

  const queue = [[begin, 0]];
  const visited = new Set();

  function canTransform(word1, word2) {
    let diffCount = 0;

    for (let i = 0; i < word1.length; i++) {
      if (word1[i] !== word2[i]) diffCount++;
      if (diffCount > 1) return false;
    }

    return diffCount === 1;
  }

  while (queue.length) {
    const [current, count] = queue.shift();

    if (current === target) return count;

    for (const word of words) {
      if (!visited.has(word) && canTransform(current, word)) {
        visited.add(word);
        queue.push([word, count + 1]);
      }
    }
  }

  return 0;
}

console.log(solution('hit', 'cog', ['hot', 'lot', 'dog', 'dot', 'log', 'cog']));
