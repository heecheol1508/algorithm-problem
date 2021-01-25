function reversing(w) {
    let reversed = '';

    for (let b of w) {
        reversed += (b === '(' ? ')' : '(');
    }
    return reversed;
}


function isCorrect(w) {
    let bracket_balance = 0;

    for (let i = 0; i < w.length; i++) {
        bracket_balance += (w[i] === '(' ? 1 : -1);
        if (bracket_balance < 0) {
            return false;
        }
    } return true;
}


function lastIndex(w) {
    let bracket_balance = 0;

    for (let i = 0; i < w.length; i++) {
        bracket_balance += (w[i] === '(' ? 1 : -1);
        if (!bracket_balance) {
            return i + 1;
        }
    }
}


function processing(w) {
    let u, v, k;

    if (!w) return '';

    k = lastIndex(w);
    u = w.slice(0, k), v = w.slice(k);
    if (isCorrect(u)) {
        return u + processing(v);
    } else {
        return '(' + processing(v) + ')' + reversing(u.slice(1, -1));
    }

}


function solution(p) {

    var answer = processing(p);
    console.log(answer);

    return answer;
}


// solution("(()())()");   // "(()())()"
solution(")(");         // "()"
solution("()))((()");   // "()(())()"
