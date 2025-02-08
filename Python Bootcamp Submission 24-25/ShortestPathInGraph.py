def Bfs_Sp(graph, start, goal):
    explored = []
    queue = [[start]]
    
    if start == goal:
        print("Same Node")
        return
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in explored:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

    print("path doesn't exist :(")
    return

if __name__ == "__main__":
    graph = {'A': ['B', 'E', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B', 'E'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    Bfs_Sp(graph, 'A', 'D')
