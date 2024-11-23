from collections import deque
def bfs(graph,start_node):
    queue=deque([start_node])
    s=set(start_node)
    while queue:
        current_node=queue.popleft()
        print(f"Node {current_node} has Visited
        print(current_node,end=" ")
        s.add(current_node)
        for neighbour in graph[current_node]:
            if neighbour not in s:
                queue.append(neighbour)
graph={'A':['B','C','D'],'B':['E','F'],'C':['G','H'],'D':['I','J'],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[]}
bfs(graph,'A')
