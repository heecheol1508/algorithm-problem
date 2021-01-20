function solution(participant, completion) {
    participant.sort();
    completion.sort();

    var i;
    for (i = 0; i < participant.length; i++) {
        if (participant[i] !== completion[i]) {
            return participant[i]
        }
    }
}