from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Initialize an empty graph using defaultdict
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge to the graph
        self.graph[u].append(v)

    def bfs(self, start):
        # Create a visited set to keep track of visited vertices
        visited = set()

        # Create a queue for BFS and enqueue the starting vertex
        queue = deque([start])

        # Mark the starting vertex as visited
        visited.add(start)

        while queue:
            # Dequeue a vertex from the queue and print it
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            # Enqueue all adjacent vertices of the dequeued vertex that are not yet visited
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Example usage:
# Create a sample graph and perform BFS starting from a specific vertex
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
print(f"BFS starting from vertex {start_vertex}:")
g.bfs(start_vertex)
