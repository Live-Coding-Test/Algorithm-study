const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
    .toString()
    .trim()
    .split('\n').map(e => e.split(' ').map(Number));

function solution() {
    const [N,M] = input[0];
    const arr = input[1];

    let count = 0;
    let left = 0;
    let right = 0;
    let sum = 0;

    while(right<=N){
        if(sum === M){
            count++
            sum -= arr[left];
            left++
        } else if (sum < M){
            sum += arr[right];
            right++;
        } else {
            sum -= arr[left];
            left++;
        }
    }

    console.log(count);

}

solution();