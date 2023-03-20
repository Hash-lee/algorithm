function solution(tickets) {
    let airlines = tickets.slice();
    airlines.sort();
    let visit = [];
    let L = airlines.length;
    for (let i=0; i < L; i++) {
        visit.push(1);
    }
    
    
    let answer = [];
    function DFS(arr) {
        if (0 < answer.length) {
            return;
        }
        if (arr.length === L + 1) {
            for (let k=1; k < arr.length; k++) {
                answer.push(arr[k][0]);
            }
            answer.push(arr[arr.length-1][1]);
            return;
        }
        else {
            for (let j=0; j < L; j++) {
                if (visit[j] === 1 && airlines[j][0] === arr[arr.length-1][1]) {
                    visit[j] = 0;
                    arr.push(airlines[j]);
                    DFS(arr);
                    arr.pop();
                    visit[j] = 1;
                }
            }
        }
    }
    DFS([["DUMMY", "ICN"]]);
    return answer;
}