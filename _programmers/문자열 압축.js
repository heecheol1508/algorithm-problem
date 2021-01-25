function splitter(str, n) {
    var result = [];
    var k;
    if (str.length % n) {
        k = str.length / n;
    } else {
        k = Math.ceil(str.length / n);
    }

    for (let j = 0; j < k; j++) {
        result.push(str.slice(n * j, n * (j + 1)));
    }
    return result;
}


function solution(s) {
    var answer = s.length;
    var len = 0;

    for (let i = 1; i < s.length / 2 + 1; i++) {
        let splits = splitter(s, i);
        let strings = [splits[0]], counts = [1];

        for (let j = 1; j < splits.length; j++) {
            if (splits[j] === strings[j - 1]) {
                strings[j - 1] = '';
                strings.push(splits[j]);
                counts.push(counts[j - 1] + 1);
                counts[j - 1] = '';
            } else if (counts[j - 1] === 1) {
                strings.push(splits[j]);
                counts.push(1);
                counts[j - 1] = '';
            } else {
                strings.push(splits[j]);
                counts.push(1);
            }
        }
        if (counts[counts.length - 1] === 1) counts[counts.length - 1] = '';
        counts.push('');

        len = strings.join('').length + counts.join('').length;

        if (len < answer) {
            answer = len;
        }
    }
    console.log(answer);

    return answer;
}


solution("abcabcdede")
