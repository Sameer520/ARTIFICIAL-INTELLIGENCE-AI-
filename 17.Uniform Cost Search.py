import heapq
def ucs(start,goal):
    l=[(0,start)]
    while l:
        cost,node=heapq.heappop(l)
        if(node==goal):
            print(cost)
            break
        for n,c in graph[node]:
            n_c=cost+c
            heapq.heappush(l,(n_c,n))
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 1)],
    'E': [('F', 3)],
    'F': []
}
ucs('A','F')
