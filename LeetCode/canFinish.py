from collections import defaultdict


def canFinish(numCourses, prerequisites) -> bool:
    graph = defaultdict(list)
    visited = [0]*numCourses
    
    for x,y in prerequisites:
        graph[x].append(y)
    
    def dfs(node):
        if visited[node] == -1:
            return False
        elif visited[node] == 1:
            return True

        visited[node] = -1

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 1
        return True

        
    for node in list(graph.keys()):
        if not dfs(node):
            return False
    return True


numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]

print(canFinish(numCourses, prerequisites))