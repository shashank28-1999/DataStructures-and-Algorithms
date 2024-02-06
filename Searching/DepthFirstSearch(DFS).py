from collections import defaultdict

class Graph:
    def __init__(self):
        # Initialize an empty graph using defaultdict
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge to the graph
        self.graph[u].append(v)

    def dfs_util(self, vertex, visited):
        # Mark the current vertex as visited and print it
        visited.add(vertex)
        print(vertex, end=" ")

        # Recur for all the adjacent vertices not yet visited
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        # Create a visited set to keep track of visited vertices
        visited = set()

        # Call the recursive helper function to perform DFS
        self.dfs_util(start, visited)

# Example usage:
# Create a sample graph and perform DFS starting from a specific vertex
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(7, 7)

start_vertex = 2
print(f"DFS starting from vertex {start_vertex}:")
g.dfs(start_vertex)
