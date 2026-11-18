
from collections import deque

graph = {
    "registration": ["assessment"],
    "assessment": ["surveyor", "settlement"],
    "surveyor": ["settlement"],
    "settlement": []
}


def bfs_shortest_path(graph, start, target):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        for neighbour in graph.get(node, []):

            if neighbour not in visited:
                visited.add(neighbour)

                queue.append(
                    (neighbour, path + [neighbour])
                )

    return None


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


print("CLAIM APPROVAL GRAPH")

for stage, next_stages in graph.items():
    print(stage, "->", next_stages)

path = bfs_shortest_path(
    graph, "registration", "settlement"
)

print("\nShortest Approval Path:")
print(" -> ".join(path) if path else "No path found")

print("\nCycle Detected:", detect_cycle(graph))

# Demonstrate a loop
cyclic_graph = {k: v[:] for k, v in graph.items()}
cyclic_graph["settlement"].append("assessment")

print("Cycle after adding a loop:",
      detect_cycle(cyclic_graph))
