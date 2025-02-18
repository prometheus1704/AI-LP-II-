
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since the graph is undirected

    def dfs_search(self, node, target, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        
        path.append(node)
        if node == target:
            print(f"DFS Path to {target}: {path}")
            return True
        visited.add(node)
        
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                if self.dfs_search(neighbor, target, path, visited):
                    return True
        
        path.pop()
        return False

    def bfs_search(self, start, target):
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            node, path = queue.popleft()
            if node == target:
                print(f"BFS Path to {target}: {path}")
                return True
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return False
    
    def full_dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.full_dfs(neighbor, visited)
    
    def full_bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Taking user input
g = Graph()
n = int(input("Enter the number of edges: "))
print("Enter the edges (format: u v):")
for _ in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

while True:
    print("\nMenu:")
    print("1. DFS Search")
    print("2. BFS Search")
    print("3. Full DFS Traversal")
    print("4. Full BFS Traversal")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        start_node = int(input("Enter the starting node: "))
        target_node = int(input("Enter the node to search: "))
        if not g.dfs_search(start_node, target_node):
            print("Node not found in DFS.")
    elif choice == 2:
        start_node = int(input("Enter the starting node: "))
        target_node = int(input("Enter the node to search: "))
        if not g.bfs_search(start_node, target_node):
            print("Node not found in BFS.")
    elif choice == 3:
        start_node = int(input("Enter the starting node: "))
        print("Full DFS Traversal:")
        g.full_dfs(start_node)
        print()
    elif choice == 4:
        start_node = int(input("Enter the starting node: "))
        print("Full BFS Traversal:")
        g.full_bfs(start_node)
        print()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


# Enter the number of edges: 5
# Enter the edges (format: u v):
# 0 1
# 0 2
# 1 3
# 2 4
# 2 5

# Menu:
# 1. DFS Search
# 2. BFS Search
# 3. Full DFS Traversal
# 4. Full BFS Traversal
# 5. Exit
# Enter your choice: 1
# Enter the starting node: 0
# Enter the node to search: 3
# DFS Path to 3: [0, 1, 3]

# Menu:
# 1. DFS Search
# 2. BFS Search
# 3. Full DFS Traversal
# 4. Full BFS Traversal
# 5. Exit
# Enter your choice: 1
# Enter the starting node: 0
# Enter the node to search: 7
# Node not found in DFS.

# Menu:
# 1. DFS Search
# 2. BFS Search
# 3. Full DFS Traversal
# 4. Full BFS Traversal
# 5. Exit
# Enter your choice: 2
# Enter the starting node: 0
# Enter the node to search: 4
# BFS Path to 4: [0, 2, 4]

# Menu:
# 1. DFS Search
# 2. BFS Search
# 3. Full DFS Traversal
# 4. Full BFS Traversal
# 5. Exit
# Enter your choice: 4
# Enter the starting node: 0
# Full BFS Traversal:
# 0 1 2 3 4 5 

# Menu:
# 1. DFS Search
# 2. BFS Search
# 3. Full DFS Traversal
# 4. Full BFS Traversal
# 5. Exit
# Enter your choice: 5
# Exiting...
