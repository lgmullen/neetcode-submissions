class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [(-cnt, task) for task,cnt in count.items()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() 
        iterate = 0
        while maxHeap or q:
            iterate +=1 
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                count, task = heapq.heappop(maxHeap)
                count += 1
                if count != 0:
                    q.append([(count, task), time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            print(time)
        print(time)
        return time 
            


            
            
        
