function solution(N, stages) {

    var onStage = [];
    for (let i of stages) {
        if (onStage[i] === undefined) {
            onStage[i] = 1;
        } else {
            onStage[i]++;
        }
    }

    var passed;
    if (onStage[N + 1] === undefined) {
        passed = 0;
    } else {
        passed = onStage[N + 1];
    }

    var rate = [];
    for (let i = N; i > 0; i--) {
        if (onStage[i] === undefined) {
            rate.push([0, i]);
        } else {
            passed += onStage[i];
            rate.push([onStage[i] / passed, i]);
        }
    }

    rate.sort(function (a, b) {
        return b[0] - a[0] || a[1] - b[1];
    })

    var answer = [];
    for (let item of rate) {
        answer.push(item[1]);
    }

    return answer;

}

solution(5, [2, 1, 2, 6, 2, 4, 3, 3]);
