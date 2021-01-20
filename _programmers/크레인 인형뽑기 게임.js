function solution(board, moves) {
    var answer = 0;
    const stack = [];

    function pick(col) {
        var row;
        for (row = 0; row < board.length; row++) {
            if (board[row][col] !== 0) {
                if (board[row][col] === stack[stack.length - 1]) {
                    stack.pop();
                    answer += 2;
                } else {
                    stack.push(board[row][col]);
                }
                board[row][col] = 0;
                return
            }
        }
    }

    for (let index of moves) {
        pick(index - 1);
    }

    return answer;
}


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])