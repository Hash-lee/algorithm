function solution(wallpaper) {
    let mn_x=99, mn_y=99, mx_x=-1, mx_y=-1;
    
    for (let i = 0; i < wallpaper.length; i++){
        for (let j=0; j < wallpaper[i].length; j++) {
            if (wallpaper[i][j] == "#") {
                if (j < mn_x) {
                    mn_x = j;
                }
                if (i < mn_y) {
                    mn_y = i;
                }
                if (mx_x < j) {
                    mx_x = j;
                }
                if (mx_y < i) {
                    mx_y = i;
                }
            }
        }
    }
    var answer = [mn_y, mn_x, mx_y + 1, mx_x + 1];
    return answer;
}