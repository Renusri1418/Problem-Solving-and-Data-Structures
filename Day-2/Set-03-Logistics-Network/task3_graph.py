
from collections import deque

# 10 hubs and their direct routes
graph = {
    "CHN": ["BLR", "HYD"],
    "BLR": ["CHN", "MYS", "GOA"],
    "HYD": ["CHN", "PUN"],
    "MYS": ["BLR"],
    "GOA": ["BLR", "MUM"],
    "PUN": ["HYD", "MUM"],
    "MUM": ["GOA", "PUN", "AHM"],
    "AHM": ["MUM", "DEL"],
    "DEL": ["AHM", "JAI"],
    "JAI": ["DEL"]
}


# BFS: Find shortest route
def bfs_shortest_route(graph, start, destination):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:

        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(
                    (neighbour, path + [neighbour])
                )

    return None


# DFS: Find reachable hubs
def dfs(graph, start):

    visited = set()
    order = []

    def visit(node):

        visited.add(node)
        order.append(node)

        for neighbour in graph[node]:

            if neighbour not in visited:
                visit(neighbour)

    visit(start)

    return order


print("LOGISTICS NETWORK ADJACENCY LIST")

for hub, routes in graph.items():
    print(hub, "->", routes)


print("\nSHORTEST ROUTE USING BFS")

route = bfs_shortest_route(graph, "CHN", "DEL")

if route:
    print(" -> ".join(route))
    print("Total hops:", len(route) - 1)
else:
    print("No route found.")


print("\nREACHABLE HUBS USING DFS")

reachable = dfs(graph, "CHN")

print(" -> ".join(reachable))
print("Total reachable hubs:", len(reachable))
