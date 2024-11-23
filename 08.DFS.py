def dfs(graph,start_node):
    visited=set()
    stack=[start_node]
    while stack:
        current_node=stack.pop()
        print(current_node,end=" ")
        visited.add(current_node)
        for n in graph[current_node]:
            if n not in visited:
                stack.append(n)
graph = {
    'A': ['B', 'C','D'],
    'B': ['A', 'E'],
    'C': ['F','A'],
    'D': ['A','G'],
    'E': [],
    'F': [],
    'G':[]
}

print("DFS traversal starting from node 'A':")
dfs(graph, 'A')
