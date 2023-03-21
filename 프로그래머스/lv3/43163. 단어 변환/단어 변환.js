function solution(begin, target, words) {
    let check = -1;
    for (let i=0; i < words.length; i++) {
        if (words[i] == target) {
            check = i;
            break;
        }
    }
    if (check === -1) {
        return 0;
    }
    
    const L = begin.length;
    let visit = Array.from({length: words.length}, ()=> 999);
    let Q = [[begin, 0]];
    let front = -1;
    let rear = 0;
    let word, move;
    while (front < rear) {
        front++;
        [word, move] = Q[front];
        if (word === target) {
            return move;
        }
        for (let idx=0; idx < visit.length; idx++){
            if (move < visit[idx]) {
                let temp = 0;
                for (let s=0; s < L; s++) {
                    if (word[s] === words[idx][s]) {
                        temp++;
                    }
                }
                if (temp === L - 1) {
                    visit[idx] = move + 1;
                    rear++;
                    Q.push([words[idx], move+1]);
                }
            }
        }
    }
    if (visit[check] === 999) {
        return 0;
    }
    return visit[check];
}