function solution(s) {
  const obj = {
    '}': '{',
    ']': '[',
    ')': '(',
  };

  const isCorrect = (string) => {
    const stack = [];
    for (const char of string) {
      if ('{[('.includes(char)) stack.push(char);
      else if (obj[char] !== stack.pop()) return false;
    }
    return stack.length ? false : true;
  };

  const rotate = (string) => string.substringing(1) + string[0];

  let result = 0;
  for (let i = 0; i < s.length; i++) {
    s = rotate(s);

    result += isCorrect(s) ? 1 : 0;
  }
  return result;
}

console.log(solution('[](){}'));
