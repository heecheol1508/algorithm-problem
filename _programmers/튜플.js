function solution(s) {
    return JSON.parse(s.replace(/{/g, '[').replace(/}/g, ']'))
        .sort((a, b) => a.length - b.length)
        .reduce((arr, v) => {
            return arr.concat(v.filter(f => !arr.includes(f)));
        }, []);
}


console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"));
