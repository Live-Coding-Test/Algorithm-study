const input = require('fs')
    .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
    .toString()
    .trim()
    .split('\n')
    .map(e => e.split(' ').map(Number));

function solution() {
    const N = input[0][0];
    const board = input.slice(1);
    const result = [0,0,0]

    function isSameNumber(x,y,size){
        for(let i=x; i<x+size; i++){
            for(let j=y; j<y+size; j++){
                if(board[x][y] !== board[i][j]){
                    return false;
                }
            }
        }
        return true;
    }

    function recursive(x,y,size){
        if(isSameNumber(x,y,size)){
            if(board[x][y] === -1) result[0]++;
            else if(board[x][y] === 0) result[1]++;
            else if(board[x][y] === 1) result[2]++;
        } else {
            const newSize = Math.floor(size/3);
            for(let i=0; i<3; i++){
                for(let j=0; j<3; j++){
                    recursive(x+i*newSize,y+j*newSize,newSize);
                }
            }
        }
    }

    recursive(0,0,N);

    console.log(result.join('\n'));

}

solution();
