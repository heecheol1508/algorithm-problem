function solution(numbers, hand) {
    var answer = '';
    var position_x = [3, 0, 0, 0, 1, 1, 1, 2, 2, 2], position_y = [1, 0, 1, 2, 0, 1, 2, 0, 1, 2];
    position_x['*'] = 3, position_y['*'] = 0;
    position_x['#'] = 3, position_y['#'] = 2;

    function distance(a, b) {
        return Math.abs(position_x[a] - position_x[b]) + Math.abs(position_y[a] - position_y[b]);
    }

    var left = '*', right = '#';
    var side_left = [1, 4, 7], side_right = [3, 6, 9];

    for (num of numbers) {
        if (side_left.includes(num)) {
            left = num;
            answer += 'L';
        } else if (side_right.includes(num)) {
            right = num;
            answer += 'R';
        } else {
            var d_left, d_right;
            d_left = distance(left, num);
            d_right = distance(right, num);
            if (d_left < d_right) {
                left = num;
                answer += 'L';
            } else if (d_left > d_right) {
                right = num;
                answer += 'R';
            } else if (hand === 'left') {
                left = num;
                answer += 'L';
            } else {
                right = num;
                answer += 'R';
            }

        }
    }

    return answer;
}


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')
