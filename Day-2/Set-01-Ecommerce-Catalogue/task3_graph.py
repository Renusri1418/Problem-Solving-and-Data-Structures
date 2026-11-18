
from collections import deque

graph = {
    "cart": ["pricing"],
    "pricing": ["inventory"],
    "inventory": ["payment"],
    "payment": ["notification"],
    "notification": []
}

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    order = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return order


def detect_cycle(graph):
    visited = set()
    active = set()

    def dfs(node):
        visited.add(node)
        active.add(node)

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
            elif neighbour in active:
                return True

        active.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


print("MICROSERVICE DEPENDENCY GRAPH")

for service, dependencies in graph.items():
    print(service, "->", dependencies)

print("\nBFS Deployment Order:")
print(" -> ".join(bfs(graph, "cart")))

print("\nCircular Dependency:")
print(detect_cycle(graph))

# Introduce a cycle
cyclic_graph = {k: v[:] for k, v in graph.items()}
cyclic_graph["notification"].append("cart")

print("\nAfter adding notification -> cart:")
print("Circular Dependency:", detect_cycle(cyclic_graph))
