def is_safe(graph, node, color, assignment):
    """
    Check if it's safe to assign a color to a node based on constraints.
    """
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, node, assignment):
    """
    Solve the graph coloring problem using backtracking.
    """
    # If all nodes are assigned, return the solution
    if len(assignment) == len(graph):
        return assignment
    
    # Try assigning each color from the color set
    for color in colors:
        if is_safe(graph, node, color, assignment):
            assignment[node] = color  # Assign the color
            
            # Recur to assign colors to the next node
            next_node = next((n for n in graph if n not in assignment), None)
            if next_node is None or graph_coloring(graph, colors, next_node, assignment):
                return assignment
            
            # Backtrack
            del assignment[node]
    
    return None  # No valid coloring found

# Example usage
if __name__ == "__main__":
    # Example graph (adjacency list representation)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    
    # Set of available colors
    colors = ['Red', 'Green', 'Blue']
    
    # Start coloring
    solution = graph_coloring(graph, colors, next(iter(graph)), {})
    
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution exists.")
