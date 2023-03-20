function solution(maps) {
    const R = maps.length;
    const C = maps[0].length;
    let visit = []
    for (let i=0; i<maps.length; i++) {
        visit.push(maps[i].slice());
    }
    let Q = [];
    let front = -1;
    let rear = 0;
    Q.push([0, 0, 1]);
    visit[0][0] = 0;
    
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    let r, c, move, k, nr, nc;
    while (front < rear) {
        front++;
        [r, c, move] = Q[front];
        if (r == R-1 && c == C-1) {
            return move
        }
        for (k=0; k < 4; k++) {
            nr = r + dr[k];
            nc = c + dc[k];
            if (0 <= nr && nr < R && 0 <= nc && nc < C && visit[nr][nc] === 1) {
                visit[nr][nc] = 0;
                Q.push([nr, nc, move+1]);
                rear++;
            }
        }
    }
    return -1;
}