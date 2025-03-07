function solution(n, lost, reserve) {
  lost.sort();
  reserve.sort();
  let arr = [...lost];
  lost.map((item) => {
    if (reserve.includes(item)) {
      arr.splice(arr.indexOf(item), 1);
      reserve.splice(reserve.indexOf(item), 1);
    }
  });
  let newArr = [...arr];

  for (let i = 0; i < arr.length; i++) {
    if (reserve.includes(arr[i] - 1) || reserve.includes(arr[i] + 1)) {
      if (reserve.includes(arr[i] - 1)) {
        reserve.splice(reserve.indexOf(arr[i] - 1), 1);
        newArr.shift();
        continue;
      }
      reserve.splice(reserve.indexOf(arr[i] + 1), 1);
      newArr.shift();
    }
  }
  return n - newArr.length;
}
