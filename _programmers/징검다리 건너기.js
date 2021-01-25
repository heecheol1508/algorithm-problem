function solution(stones, k) {
    var numbers = Array.from(new Set(stones)).sort((a, b) => a - b);
    var answer = 0;
    var gap = numbers[0];

    function isPass() {
        let cur = -1;
        do {
            let flag = false;
            for (let i = cur + k; i > cur; i--) {
                if (stones[i]) {
                    cur = i;
                    flag = true;
                    break;
                }
            }
            if (!flag) return false;
        } while (cur + k < stones.length)

        return true;
    }

    for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < stones.length; j++) {
            if (stones[j]) {
                stones[j] -= gap;
            }
        }

        answer = numbers[i];
        if (!isPass()) return answer;

        gap = numbers[i + 1] - numbers[i];
    }
}


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3);
