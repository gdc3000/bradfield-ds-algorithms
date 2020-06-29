import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #check for empty list
        if not times:
            return -1
        
        #build times dict by node
        times_by_node = self.assembleTimesByNode(times, N)
    
        #dijkstra's shortest path
        time_to = {node: float('infinity') for node in range(1,N+1)}
        time_to[K] = 0
        
        pq = [(0, K)]
        while len(pq) > 0:
            curr_time, curr_node = heapq.heappop(pq)
            
            if curr_time > time_to[curr_node]:
                continue
            
            for next_node, time_to_next in times_by_node[curr_node].items():
                total_time = curr_time + time_to_next
                
                if total_time < time_to[next_node]:
                    time_to[next_node] = total_time
                    heapq.heappush(pq, (total_time, next_node))
        
        #validate that all nodes have been reached and find max time.
        max_time = 0
        for k in time_to.keys():
            if time_to[k] > max_time:
                max_time = time_to[k]
        if max_time == float('infinity'):
            return -1
        else: 
            return max_time
    
    def assembleTimesByNode(self, times: List[List[int]], N: int) -> dict():
        times_by_node = dict()
        for i in range(1,N+1): 
            times_by_node[i] = {}
        for source_node, next_node, time_to_next in times:
            times_by_node[source_node].update( {next_node : time_to_next} )
        return times_by_node

test_list = [[2,1,1],[2,3,1],[3,4,1]]
test_N = 4
test_K = 2
assert Solution().networkDelayTime(test_list, test_N, test_K) == 2


test_list = [[2,1,1],[2,3,1],[3,4,1],[4,5,1]]
test_N = 5
test_K = 2
assert Solution().networkDelayTime(test_list, test_N, test_K) == 3

test_list = [[1,2,1]]
test_N = 5
test_K = 2
assert Solution().networkDelayTime(test_list, test_N, test_K) == -1