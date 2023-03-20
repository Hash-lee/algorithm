function solution(bridge_length, weight, truck_weights) {
    let on_weight = 0;
    let on_time = 0;
    let on_bridge = [];
    let t, w;
    
    
    let trucks = truck_weights.slice();
    while (0 < trucks.length) {
        on_time++;
        if (on_bridge.length > 0 && on_bridge[0][0] + bridge_length <= on_time) {
            [t, w] = on_bridge.shift();
            on_weight -= w;
        }
        if (trucks[0] + on_weight <= weight){
            w = trucks.shift();
            on_weight += w;
            on_bridge.push([on_time, w]);
        } else {
            on_time = on_bridge[0][0] + bridge_length - 1;
        }
    }
    
    return on_bridge[on_bridge.length-1][0] + bridge_length;
}