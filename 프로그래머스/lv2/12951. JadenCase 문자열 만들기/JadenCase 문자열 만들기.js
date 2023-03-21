function solution(s) {
    let answer = '';
    let flag = 1;
    for (let i=0; i < s.length; i++) {
        if (flag) {
            answer += s[i].toUpperCase();
            flag = 0;
        } else {
            answer += s[i].toLowerCase();
        }
        if (s[i]===" ") {
            flag = 1
        }
    }
    
    return answer;
}