function solution(n, m, section) {
    var painted = -1;
    var answer = 0;
    
    for (let i=0; i < section.length; i++) {
        if (painted < section[i]) {
            answer++;
            painted = section[i] + m - 1;
        }
    }
    return answer;
}