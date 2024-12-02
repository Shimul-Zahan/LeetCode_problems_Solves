import heapq

def a_star_search(graph, start, goal, heuristic):
    # Priority queue for open set
    open_set = []
    heapq.heappush(open_set, (0, start))  # (f(n), node)
    
    # Maps to track costs and paths
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    came_from = {}  # To reconstruct the path
    
    while open_set:
        # Node with the smallest f(n)
        _, current = heapq.heappop(open_set)
        
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        # Explore neighbors
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            
            if tentative_g_score < g_score[neighbor]:
                # Update path and scores
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                
                # Add neighbor to open set
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

# Example graph (Adjacency list with weights)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 6)],
    'G': []
}

# Example heuristic (Straight-line distances to goal)
heuristic = {
    'A': 6, 'B': 4, 'C': 5,
    'D': 2, 'E': 2, 'F': 6,
    'G': 0
}

# Run A* search
start = 'A'
goal = 'G'
path = a_star_search(graph, start, goal, heuristic)
print("Shortest path:", path)
