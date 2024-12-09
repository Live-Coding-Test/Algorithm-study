function solution(k, tangerine) {
  var answer = 0;
  tangerine.sort((a, b) => a - b);

  let tMap = new Map();

  for (let i = 0; i < tangerine.length; i++) {
    tMap.set(
      tangerine[i],
      (tMap.has(tangerine[i]) ? tMap.get(tangerine[i]) : 0) + 1
    );
  }

  valueArr = [];
  for (let [_, value] of tMap) {
    valueArr.push(value);
  }
  valueArr.sort((a, b) => b - a);

  for (let i = 0; i < valueArr.length; i++) {
    if (k <= 0) break;
    else {
      k -= valueArr[i];
      answer++;
    }
  }

  return answer;
}

console.log(solution(1, [1]));
