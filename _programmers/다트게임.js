function solution(dartResult) {
    var answer = 0;
    var splits = dartResult.split(/(S|D|T)/);

    var numbers = [];
    var index = -1;
    for (let item of splits) {
        if (!isNaN(parseInt(item))) {
            numbers.push(parseInt(item));
            index++;
        } else if (item[0] === 'S') {
            continue;
        } else if (item[0] === 'D') {
            numbers[index] **= 2;
        } else if (item[0] === 'T') {
            numbers[index] **= 3;
        } else if (item[0] === '#') {
            numbers[index] *= -1;
            if (item.length !== 1) {
                let num = item.slice(1);
                numbers.push(parseInt(num));
                index++;
            }
        } else if (item[0] === '*') {
            numbers[index] *= 2;
            numbers[index - 1] *= 2;
            if (item.length !== 1) {
                let num = item.slice(1);
                numbers.push(parseInt(num));
                index++;
            }
        }
    }

    const reducer = (a, b) => a + b;
    answer = numbers.reduce(reducer);

    return answer;
}


solution("1D2S0T");
