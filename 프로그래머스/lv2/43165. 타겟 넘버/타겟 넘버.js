function solution(numbers, target) {
    let answer = 0;
    function proceed(arr, idx, now_sum) {
        if (idx == arr.length) {
            if (now_sum == target) {
                answer++;
            }
            return;
        }
        proceed(arr, idx + 1, now_sum + arr[idx]);
        proceed(arr, idx + 1, now_sum - arr[idx]);
    }
    proceed(numbers, 0, 0);
    
    return answer;
}