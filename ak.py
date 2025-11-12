import heapq
pQueue =[]
heapq.heappush(pQueue,10)
heapq.heappush(pQueue,20)
heapq.heappush(pQueue,15)
print (pQueue[0])
print(heapq.heappop(pQueue))
print(pQueue[0]) 