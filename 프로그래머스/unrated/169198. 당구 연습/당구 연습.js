function solution(m, n, startX, startY, balls) {
    const width = m;
    const height = n;
    let endX, endY;
    let answer = [];
    for (let i=0; i<balls.length; i++) {
        [endX, endY] = balls[i];
        if (startX != endX && startY != endY) {
            answer.push(Math.min(
                (startX + endX)**2 + (endY - startY)**2,
                (width*2 - endX - startX)**2 + (endY - startY)**2,
                (endX - startX)**2 + (height*2 - endY - startY)**2,
                (endX - startX)**2 + (startY + endY)**2
            ))
        } else if (startX == endX) {
            let sameX;
            if (startY < endY) {
                sameX = (startY + endY)**2;
            } else {
                sameX = (height*2 - startY - endY)**2;
            }
            answer.push(Math.min(
                sameX,
                (startX + endX)**2 + (endY - startY)**2,
                (width*2 - endX - startX)**2 + (endY - startY)**2,
            ))    
        } else if (startY == endY) {
            let sameY;
            if (startX < endX) {
                sameY = (startX + endX)**2;
            } else {
                sameY = (width*2 - startX - endX)**2;
            }
            answer.push(Math.min(
                sameY,
                (endX - startX)**2 + (height*2 - endY - startY)**2,
                (endX - startX)**2 + (startY + endY)**2
            ))
        }
    }
    return answer;
}