function solution(food) {
  var answer = '';
  let arr = food.slice(1).map((x) => Math.floor(x / 2));

  let temp = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      temp.push((i + 1).toString().repeat(arr[i]));
    }
  }

  return (answer = temp.join('') + '0' + temp.reverse().join(''));
}

console.log(solution([1, 3, 4, 6]));
