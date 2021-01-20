function solution(answers) {

    var a1 = [1, 2, 3, 4, 5];
    var a2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    var score1 = answers.filter((a, i) => a === a1[i % a1.length]).length;
    var score2 = answers.filter((a, i) => a === a2[i % a2.length]).length;
    var score3 = answers.filter((a, i) => a === a3[i % a3.length]).length;
    var max = Math.max(score1, score2, score3);

    var answer = [];
    if (score1 === max) answer.push(1);
    if (score2 === max) answer.push(2);
    if (score3 === max) answer.push(3);

    console.log(answer);

    return answer;
}

solution([1, 3, 2, 4, 2])
