from collections import deque

def generate_graph(grid, rows, cols):
    node_connections = {}

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                continue

            current_position = (i, j)
            connected_nodes = []

            if i > 0 and grid[i-1][j] == 1:
                connected_nodes.append((i-1, j))
            if i < rows-1 and grid[i+1][j] == 1:
                connected_nodes.append((i+1, j))
            if j > 0 and grid[i][j-1] == 1:
                connected_nodes.append((i, j-1))
            if j < cols-1 and grid[i][j+1] == 1:
                connected_nodes.append((i, j+1))

            node_connections[current_position] = connected_nodes

    return node_connections

def calculate_shortest_distance(graph, end, queue, visited):
    if not queue:
        return -1

    current_position, distance = queue.popleft()

    if current_position == end:
        return distance

    for neighbor in graph[current_position]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, distance+1))

    return calculate_shortest_distance(graph, end, queue, visited)

def main():
    rows = int(input())
    cols = int(input())
    start_position = tuple(map(int, input().split()))
    end_position = tuple(map(int, input().split()))

    input_grid = [list(map(int, input()[1:-1].split(','))) for _ in range(rows)]
    node_connections = generate_graph(input_grid, rows, cols)

    traversal_queue = deque()
    visited_nodes = set()

    if start_position in node_connections:
        visited_nodes = set([start_position])
        traversal_queue = deque([(start_position, 0)])

    min_dist = calculate_shortest_distance(node_connections, end_position, traversal_queue, visited_nodes)

    if min_dist == -1:
        print("There is no possible path")
    else:
        print("The minimum distance is", min_dist)

if __name__ == "__main__":
    main()
